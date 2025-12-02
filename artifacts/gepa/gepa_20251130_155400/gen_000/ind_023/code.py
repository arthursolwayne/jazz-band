
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 1.125), (38, 1.5), (42, 1.5),
    (36, 2.125), (38, 2.5), (42, 2.5),
    (36, 3.125), (38, 3.5), (42, 3.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (walking line, chromatic approaches)
bass_notes = [
    (62, 1.5), (60, 1.875), (63, 2.25), (64, 2.625),
    (62, 2.625), (60, 2.875), (63, 3.25), (64, 3.625),
    (62, 3.625), (60, 3.875), (63, 4.25), (64, 4.625),
    (62, 4.625), (60, 4.875), (63, 5.25), (64, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (64, 2.0), (67, 2.0), (69, 2.0), (71, 2.0),  # Dm7
    (64, 2.5), (67, 2.5), (69, 2.5), (71, 2.5),  # Dm7
    # Bar 3 (3.0 - 4.5s)
    (64, 3.5), (67, 3.5), (72, 3.5), (74, 3.5),  # G7
    (64, 4.0), (67, 4.0), (72, 4.0), (74, 4.0),  # G7
    # Bar 4 (4.5 - 6.0s)
    (64, 5.0), (67, 5.0), (69, 5.0), (71, 5.0),  # Dm7
    (64, 5.5), (67, 5.5), (69, 5.5), (71, 5.5)   # Dm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Dante (melody - one short motif, make it sing)
sax_notes = [
    (62, 1.5), (64, 1.75), (62, 2.0), (65, 2.25),  # Motif
    (62, 2.5), (64, 2.75), (62, 3.0), (65, 3.25),  # Repeat
    (62, 3.5), (64, 3.75), (62, 4.0), (65, 4.25),  # Repeat
    (62, 4.5), (64, 4.75), (62, 5.0), (65, 5.25)   # Repeat
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
