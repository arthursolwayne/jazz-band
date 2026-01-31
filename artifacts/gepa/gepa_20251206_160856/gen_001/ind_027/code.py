
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
    # Kick on 1 and 3
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    for beat in range(8):
        note = pretty_midi.Note(velocity=80, pitch=42, start=start + beat * 0.125, end=start + beat * 0.125 + 0.05)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: F - G - A - Bb
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # F root (MIDI 53), G (MIDI 55)
        bass_notes = [53, 55]
    elif bar == 3:
        # A (MIDI 57), Bb (MIDI 58)
        bass_notes = [57, 58]
    elif bar == 4:
        # C (MIDI 60), D (MIDI 62)
        bass_notes = [60, 62]
    for i, note in enumerate(bass_notes):
        note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start + i * 0.375, end=start + i * 0.375 + 0.1)
        bass.notes.append(note_obj)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
bar = 2
start = bar * 1.5
piano_notes = [53, 58, 60, 64]
for note in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 1.5)
    piano.notes.append(note_obj)

# Bar 3: G7 (G, B, D, F)
bar = 3
start = bar * 1.5
piano_notes = [55, 59, 62, 53]
for note in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 1.5)
    piano.notes.append(note_obj)

# Bar 4: Am7 (A, C, E, G)
bar = 4
start = bar * 1.5
piano_notes = [57, 60, 64, 59]
for note in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 1.5)
    piano.notes.append(note_obj)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    for beat in range(8):
        note = pretty_midi.Note(velocity=80, pitch=42, start=start + beat * 0.125, end=start + beat * 0.125 + 0.05)
        drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - A - Bb - F (MIDI 53, 58, 58, 53)
# Play it on beat 1 of bar 2, then leave it hanging until beat 3 of bar 3, then finish it

# First note at bar 2, beat 0
sax_note1 = pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.5 + 0.375)
sax.notes.append(sax_note1)

# Second note at bar 2, beat 0.75 (halfway between beat 1 and 2)
sax_note2 = pretty_midi.Note(velocity=110, pitch=58, start=1.5 + 0.375 * 0.75, end=1.5 + 0.375 * 0.75 + 0.375)
sax.notes.append(sax_note2)

# Third note at bar 3, beat 1.5 (wait until this point)
sax_note3 = pretty_midi.Note(velocity=110, pitch=58, start=3.0 + 0.75, end=3.0 + 0.75 + 0.375)
sax.notes.append(sax_note3)

# Final note at bar 3, beat 2.25
sax_note4 = pretty_midi.Note(velocity=110, pitch=53, start=3.0 + 1.125, end=3.0 + 1.125 + 0.375)
sax.notes.append(sax_note4)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
