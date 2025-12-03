
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5s to 3.0s)

# Marcus: Walking line in D (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5), (40, 1.75), (38, 2.0), (41, 2.25),
    (43, 2.5), (41, 2.75), (38, 3.0), (40, 3.25)
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: G7 (D, F#, G, B)
piano_notes = [
    (65, 1.5), (67, 1.5), (69, 1.5), (71, 1.5),
    (65, 1.75), (67, 1.75), (69, 1.75), (71, 1.75),
    (65, 2.0), (67, 2.0), (69, 2.0), (71, 2.0),
    (65, 2.25), (67, 2.25), (69, 2.25), (71, 2.25)
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 3: Full quartet (3.0s to 4.5s)

# Marcus: Walking line in D (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 3.0), (40, 3.25), (38, 3.5), (41, 3.75),
    (43, 4.0), (41, 4.25), (38, 4.5), (40, 4.75)
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Am7 (A, C, E, G)
piano_notes = [
    (69, 3.0), (71, 3.0), (74, 3.0), (76, 3.0),
    (69, 3.25), (71, 3.25), (74, 3.25), (76, 3.25),
    (69, 3.5), (71, 3.5), (74, 3.5), (76, 3.5),
    (69, 3.75), (71, 3.75), (74, 3.75), (76, 3.75)
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 4: Full quartet (4.5s to 6.0s)

# Marcus: Walking line in D (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 4.5), (40, 4.75), (38, 5.0), (41, 5.25),
    (43, 5.5), (41, 5.75), (38, 6.0), (40, 6.25)
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cmaj7 (C, E, G, B)
piano_notes = [
    (60, 4.5), (64, 4.5), (67, 4.5), (71, 4.5),
    (60, 4.75), (64, 4.75), (67, 4.75), (71, 4.75),
    (60, 5.0), (64, 5.0), (67, 5.0), (71, 5.0),
    (60, 5.25), (64, 5.25), (67, 5.25), (71, 5.25)
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375),
    (36, 6.75), (38, 7.125), (42, 7.125)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Dante: Sax solo (Bar 2-4)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start the motif
sax_notes = [
    (65, 1.5), (67, 1.75), (67, 2.0), (65, 2.25)
]
for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Bar 3: Leave it hanging
sax_notes = [
    (67, 3.0), (65, 3.25), (67, 3.5), (66, 3.75)
]
for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Bar 4: Come back and finish it
sax_notes = [
    (65, 4.5), (67, 4.75), (67, 5.0), (65, 5.25)
]
for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
