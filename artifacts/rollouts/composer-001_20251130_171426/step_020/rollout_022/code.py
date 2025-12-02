
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, chromatic approaches
bass_notes = [
    (48, 1.5), (49, 1.75), (47, 2.0), (45, 2.25),   # Fm7
    (48, 2.5), (49, 2.75), (50, 3.0), (52, 3.25),   # Bb7
    (48, 3.5), (49, 3.75), (47, 4.0), (45, 4.25),   # Fm7
    (48, 4.5), (50, 4.75), (52, 5.0), (53, 5.25)    # D7
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (44, 2.0), (47, 2.0), (50, 2.0), (53, 2.0),  # Fm7 (bar 2)
    (50, 3.0), (53, 3.0), (55, 3.0), (58, 3.0),  # Bb7 (bar 3)
    (44, 4.0), (47, 4.0), (50, 4.0), (53, 4.0),  # Fm7 (bar 4)
    (50, 5.0), (53, 5.0), (55, 5.0), (58, 5.0)   # D7 (bar 4)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums: Continue
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.25), (42, 2.375), (42, 2.5), (42, 2.625),
    (36, 2.75), (38, 3.125), (42, 2.75), (42, 2.875), (42, 3.0), (42, 3.125),
    (36, 3.5), (38, 3.875), (42, 3.5), (42, 3.625), (42, 3.75), (42, 3.875),
    (36, 4.25), (38, 4.625), (42, 4.25), (42, 4.375), (42, 4.5), (42, 4.625),
    (36, 4.75), (38, 5.125), (42, 4.75), (42, 4.875), (42, 5.0), (42, 5.125)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Motif (bar 2)
# Start on F (48), short motif: F - Ab - D - F
sax_notes = [
    (48, 1.5), (50, 1.75), (55, 2.0), (48, 2.25)  # F - Ab - D - F
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: Second pass (bar 4)
# Repeat motif but with a twist: F - Ab - D - Eb
sax_notes = [
    (48, 4.5), (50, 4.75), (55, 5.0), (52, 5.25)  # F - Ab - D - Eb
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
