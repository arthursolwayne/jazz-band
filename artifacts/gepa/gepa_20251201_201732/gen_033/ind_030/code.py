
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
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375),  # Hihat on 4
]
for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),  # D2 (root)
    (41, 1.875, 0.375),  # F (chromatic approach)
    (43, 2.25, 0.375),  # G2 (fifth)
    (38, 2.625, 0.375),  # D2 (root)
]
for note_number, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    (50, 1.5, 0.375),  # D
    (53, 1.5, 0.375),  # F
    (58, 1.5, 0.375),  # A
    (60, 1.5, 0.375),  # C
]
for note_number, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    piano.notes.append(note)

# Sax: Melody - short motif, make it sing. Start it, leave it hanging.
sax_notes = [
    (62, 1.5, 0.375),  # E (Dm scale)
    (65, 1.875, 0.375),  # G
    (67, 2.25, 0.375),  # A
    (69, 2.625, 0.375),  # Bb
]
for note_number, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (43, 3.0, 0.375),  # G2 (fifth)
    (41, 3.375, 0.375),  # F (chromatic approach)
    (38, 3.75, 0.375),  # D2 (root)
    (40, 4.125, 0.375),  # E (chromatic approach)
]
for note_number, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Am7 (A C E G)
piano_notes = [
    (65, 3.0, 0.375),  # A
    (69, 3.0, 0.375),  # C
    (72, 3.0, 0.375),  # E
    (76, 3.0, 0.375),  # G
]
for note_number, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    piano.notes.append(note)

# Sax: Melody - continuation of the motif
sax_notes = [
    (67, 3.0, 0.375),  # A
    (69, 3.375, 0.375),  # Bb
    (65, 3.75, 0.375),  # G
    (62, 4.125, 0.375),  # E
]
for note_number, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.375),  # Hihat on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.375),  # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.375),  # Hihat on 4
]
for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (40, 4.5, 0.375),  # E (chromatic approach)
    (38, 4.875, 0.375),  # D2 (root)
    (41, 5.25, 0.375),  # F (chromatic approach)
    (43, 5.625, 0.375),  # G2 (fifth)
]
for note_number, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Dm7 (D F A C)
piano_notes = [
    (50, 4.5, 0.375),  # D
    (53, 4.5, 0.375),  # F
    (58, 4.5, 0.375),  # A
    (60, 4.5, 0.375),  # C
]
for note_number, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    piano.notes.append(note)

# Sax: Melody - complete the motif
sax_notes = [
    (62, 4.5, 0.375),  # E
    (65, 4.875, 0.375),  # G
    (67, 5.25, 0.375),  # A
    (65, 5.625, 0.375),  # G (resolve on the last)
]
for note_number, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.375),  # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375),  # Hihat on 4
]
for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
