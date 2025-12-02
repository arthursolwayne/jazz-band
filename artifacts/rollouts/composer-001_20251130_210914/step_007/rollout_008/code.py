
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
    (36, 0.0), (38, 0.375), (42, 0.375), (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    (62, 1.5), (64, 1.875), (63, 2.25), (60, 2.625),
    (62, 2.625), (64, 2.875), (63, 3.25), (60, 3.625),
    (62, 3.625), (64, 3.875), (63, 4.25), (60, 4.625),
    (62, 4.625), (64, 4.875), (63, 5.25), (60, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: comping on 2 and 4 with 7th chords
piano_notes = [
    (60, 2.0, 62), (65, 2.0, 67),  # Dm7
    (60, 2.0, 62), (65, 2.0, 67),
    (60, 3.0, 62), (65, 3.0, 67),  # Dm7 again
    (60, 3.0, 62), (65, 3.0, 67),
    (60, 4.0, 62), (65, 4.0, 67),  # Dm7 again
    (60, 4.0, 62), (65, 4.0, 67)
]
for pitch, time, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration))

# Sax: short motif, make it sing
sax_notes = [
    (62, 1.5, 0.5),  # E
    (60, 2.0, 0.5),  # D
    (62, 2.5, 0.5),  # E
    (67, 3.0, 0.5),  # G
    (62, 3.5, 0.5),  # E
    (60, 4.0, 0.5),  # D
    (62, 4.5, 0.5),  # E
    (67, 5.0, 0.5)   # G
]
for pitch, time, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration))

# Drums: continue after bar 1
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875), (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375), (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
