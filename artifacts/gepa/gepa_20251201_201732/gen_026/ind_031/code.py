
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
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm (D2-G2, MIDI 38-43)
bass_notes = [
    (38, 1.5), (40, 1.875), (42, 2.25), (43, 2.625),
    (38, 3.0), (40, 3.375), (42, 3.75), (43, 4.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    (53, 1.5), (60, 1.5), (64, 1.5), (65, 1.5),
    (60, 1.5), (64, 1.5), (65, 1.5)  # resolve on the last
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Sax: Motif - start it, leave it hanging
# Fm motif: F, Ab, G, Ab
sax_notes = [
    (53, 1.5), (56, 1.875), (57, 2.25), (56, 2.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm (D2-G2, MIDI 38-43)
bass_notes = [
    (43, 3.0), (38, 3.375), (40, 3.75), (42, 4.125),
    (38, 4.5), (40, 4.875), (42, 5.25), (43, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar
# Bar 3: Bbm7 (Bb, Db, F, Ab)
piano_notes = [
    (58, 3.0), (62, 3.0), (53, 3.0), (60, 3.0),
    (60, 3.0), (62, 3.0), (60, 3.0)  # resolve on the last
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Sax: Continue motif
# F, Ab, G, Ab
sax_notes = [
    (53, 3.0), (56, 3.375), (57, 3.75), (56, 4.125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm (D2-G2, MIDI 38-43)
bass_notes = [
    (38, 4.5), (40, 4.875), (42, 5.25), (43, 5.625),
    (38, 6.0), (40, 6.375), (42, 6.75), (43, 7.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    (60, 4.5), (64, 4.5), (67, 4.5), (58, 4.5),
    (60, 4.5), (64, 4.5), (67, 4.5)  # resolve on the last
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Sax: Finish the motif
# F, Ab, G, Ab
sax_notes = [
    (53, 4.5), (56, 4.875), (57, 5.25), (56, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375),
    (36, 6.75), (38, 7.125), (42, 7.125)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
