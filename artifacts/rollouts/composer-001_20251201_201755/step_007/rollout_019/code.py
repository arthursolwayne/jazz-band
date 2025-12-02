
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
for bar in range(1):
    start = bar * 1.5
    kick_time = start + 0.0
    snare_time = start + 0.75
    hihat_time = start + 0.0
    for i in range(8):
        hihat_time = start + (i * 0.125)
        note = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.0625)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.0625)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.0625)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in D (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Piano: Open voicings, different chord each bar, resolve on the last
# Sax: Short motif, start it, leave it hanging, come back and finish it

# Bass
bass_notes = [
    (38, 1.5, 1.5 + 0.25),  # D2
    (40, 1.75, 1.75 + 0.25),  # F#2
    (43, 2.0, 2.0 + 0.25),  # A2
    (42, 2.25, 2.25 + 0.25),  # G2
]
for pitch, start, end in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano
# Bar 2: D7 (D F# A C#)
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.25)  # D4
note2 = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.5 + 0.25)  # F#4
note3 = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.25)  # A4
note4 = pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=1.5 + 0.25)  # C#4
piano.notes.extend([note, note2, note3, note4])

# Sax: short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    (62, 1.5, 1.5 + 0.125),  # D4
    (67, 1.625, 1.625 + 0.125),  # F#4
    (62, 1.75, 1.75 + 0.125),  # D4
    (67, 1.875, 1.875 + 0.125),  # F#4
]
for pitch, start, end in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in D (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Piano: Open voicings, different chord each bar, resolve on the last
# Sax: short motif, start it, leave it hanging, come back and finish it

# Bass
bass_notes = [
    (43, 3.0, 3.0 + 0.25),  # A2
    (41, 3.25, 3.25 + 0.25),  # G#2
    (42, 3.5, 3.5 + 0.25),  # G2
    (40, 3.75, 3.75 + 0.25),  # F#2
]
for pitch, start, end in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano
# Bar 3: G7 (G B D F#)
note = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.0 + 0.25)  # G4
note2 = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.0 + 0.25)  # B4
note3 = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.0 + 0.25)  # A4
note4 = pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.0 + 0.25)  # C#4
piano.notes.extend([note, note2, note3, note4])

# Sax: motif continuation
sax_notes = [
    (67, 3.0, 3.0 + 0.125),  # F#4
    (71, 3.125, 3.125 + 0.125),  # A4
    (67, 3.25, 3.25 + 0.125),  # F#4
    (71, 3.375, 3.375 + 0.125),  # A4
]
for pitch, start, end in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in D (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Piano: Open voicings, different chord each bar, resolve on the last
# Sax: finish the motif

# Bass
bass_notes = [
    (38, 4.5, 4.5 + 0.25),  # D2
    (40, 4.75, 4.75 + 0.25),  # F#2
    (43, 5.0, 5.0 + 0.25),  # A2
    (42, 5.25, 5.25 + 0.25),  # G2
]
for pitch, start, end in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano
# Bar 4: D7 (D F# A C#)
note = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.5 + 0.25)  # D4
note2 = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.5 + 0.25)  # F#4
note3 = pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.5 + 0.25)  # A4
note4 = pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.5 + 0.25)  # C#4
piano.notes.extend([note, note2, note3, note4])

# Sax: finish the motif
sax_notes = [
    (62, 4.5, 4.5 + 0.125),  # D4
    (67, 4.625, 4.625 + 0.125),  # F#4
    (62, 4.75, 4.75 + 0.125),  # D4
    (67, 4.875, 4.875 + 0.125),  # F#4
]
for pitch, start, end in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    kick_time = start + 0.0
    snare_time = start + 0.75
    hihat_time = start + 0.0
    for i in range(8):
        hihat_time = start + (i * 0.125)
        note = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.0625)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.0625)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.0625)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
