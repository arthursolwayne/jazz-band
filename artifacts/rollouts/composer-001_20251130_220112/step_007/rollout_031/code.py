
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    (17, 1.5, 0.375), (18, 1.875, 0.375), (15, 2.25, 0.375), (17, 2.625, 0.375), # Bar 2
    (19, 3.0, 0.375), (20, 3.375, 0.375), (18, 3.75, 0.375), (19, 4.125, 0.375), # Bar 3
    (17, 4.5, 0.375), (18, 4.875, 0.375), (15, 5.25, 0.375), (17, 5.625, 0.375)  # Bar 4
]
for note, start, duration in bass_notes:
    b = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(b)

# Piano: comping on 2 and 4 with 7th chords
piano_notes = {
    1.875: [(41, 100), (43, 100)],  # F7
    3.375: [(41, 100), (43, 100)],  # F7
    4.875: [(41, 100), (43, 100)]   # F7
}
for start, notes in piano_notes.items():
    for pitch, vel in notes:
        p = pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.375)
        piano.notes.append(p)

# Sax: Short motif starting at 1.5s, phrases for 3 bars
sax_notes = [
    (24, 1.5, 0.375), (26, 1.875, 0.375), (24, 2.25, 0.375),  # First phrase
    (22, 2.625, 0.375), (24, 2.625, 0.375), (26, 2.625, 0.375),  # Leave it hanging
    (24, 3.0, 0.375), (26, 3.375, 0.375), (24, 3.75, 0.375),  # Return to melody
    (22, 4.125, 0.375), (24, 4.5, 0.375), (26, 4.875, 0.375)   # Finish
]
for note, start, duration in sax_notes:
    s = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(s)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
