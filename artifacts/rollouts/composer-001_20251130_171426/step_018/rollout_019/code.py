
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
    (36, 1.125), (38, 1.5), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5), (63, 1.75), (60, 2.0), (62, 2.25),
    (64, 2.5), (65, 2.75), (62, 3.0), (64, 3.25),
    (67, 3.5), (68, 3.75), (65, 4.0), (67, 4.25),
    (70, 4.5), (71, 4.75), (68, 5.0), (70, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (67, 1.75), (71, 1.75), (69, 1.75), (73, 1.75),  # D7
    # Bar 3
    (70, 2.75), (74, 2.75), (72, 2.75), (76, 2.75),  # F#7
    # Bar 4
    (67, 3.75), (71, 3.75), (69, 3.75), (73, 3.75),  # D7
    (70, 4.75), (74, 4.75), (72, 4.75), (76, 4.75)   # F#7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.75), (42, 1.75),
    (36, 2.25), (38, 2.5), (42, 2.5),
    (36, 3.0), (38, 3.25), (42, 3.25),
    (36, 3.75), (38, 4.0), (42, 4.0),
    (36, 4.5), (38, 4.75), (42, 4.75)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Tenor sax — one short motif, make it sing
# Start on D, then E, then B, then D
sax_notes = [
    (62, 1.5), (64, 1.75), (67, 2.0), (62, 2.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
