
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Fill the bar with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for note in [36, 38, 42]:
        if note == 36:  # Kick
            midi_time = bar * 1.5 + 0.0
            midi_note = pretty_midi.Note(velocity=100, pitch=note, start=midi_time, end=midi_time + 0.375)
            drums.notes.append(midi_note)
            midi_time = bar * 1.5 + 0.75
            midi_note = pretty_midi.Note(velocity=100, pitch=note, start=midi_time, end=midi_time + 0.375)
            drums.notes.append(midi_note)
        elif note == 38:  # Snare
            midi_time = bar * 1.5 + 0.375
            midi_note = pretty_midi.Note(velocity=100, pitch=note, start=midi_time, end=midi_time + 0.375)
            drums.notes.append(midi_note)
            midi_time = bar * 1.5 + 1.125
            midi_note = pretty_midi.Note(velocity=100, pitch=note, start=midi_time, end=midi_time + 0.375)
            drums.notes.append(midi_note)
        elif note == 42:  # Hihat
            for i in range(4):
                midi_time = bar * 1.5 + i * 0.375
                midi_note = pretty_midi.Note(velocity=100, pitch=note, start=midi_time, end=midi_time + 0.125)
                drums.notes.append(midi_note)

# Bar 2: All instruments in
# Dm7 - G7 - Cm7 - F7
# Piano: Open voicings, resolve on the last bar
note_duration = 0.375
bar_start = 1.5

# Bar 2: Dm7 (D, F, A, C)
piano_notes = [62, 64, 67, 69]
for i, pitch in enumerate(piano_notes):
    midi_note = pretty_midi.Note(velocity=100, pitch=pitch, start=bar_start + i * note_duration, end=bar_start + i * note_duration + note_duration)
    piano.notes.append(midi_note)

# Bass: D (D2) to G (G2) with chromatic approach
bass_notes = [62, 63, 64, 64]
for i, pitch in enumerate(bass_notes):
    midi_note = pretty_midi.Note(velocity=100, pitch=pitch, start=bar_start + i * note_duration, end=bar_start + i * note_duration + note_duration)
    bass.notes.append(midi_note)

# Sax: Melody starts here
# D - F - A - D (short motif)
sax_notes = [62, 64, 67, 62]
for i, pitch in enumerate(sax_notes):
    midi_note = pretty_midi.Note(velocity=100, pitch=pitch, start=bar_start + i * note_duration, end=bar_start + i * note_duration + note_duration)
    sax.notes.append(midi_note)

# Bar 3: G7 (G, B, D, F)
piano_notes = [67, 69, 71, 64]
for i, pitch in enumerate(piano_notes):
    midi_note = pretty_midi.Note(velocity=100, pitch=pitch, start=bar_start + 1.5 + i * note_duration, end=bar_start + 1.5 + i * note_duration + note_duration)
    piano.notes.append(midi_note)

# Bass: G (G2) to C (C2) with chromatic approach
bass_notes = [67, 68, 69, 69]
for i, pitch in enumerate(bass_notes):
    midi_note = pretty_midi.Note(velocity=100, pitch=pitch, start=bar_start + 1.5 + i * note_duration, end=bar_start + 1.5 + i * note_duration + note_duration)
    bass.notes.append(midi_note)

# Sax: F - A - D - F (continuation of the motif)
sax_notes = [64, 67, 62, 64]
for i, pitch in enumerate(sax_notes):
    midi_note = pretty_midi.Note(velocity=100, pitch=pitch, start=bar_start + 1.5 + i * note_duration, end=bar_start + 1.5 + i * note_duration + note_duration)
    sax.notes.append(midi_note)

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [60, 62, 67, 65]
for i, pitch in enumerate(piano_notes):
    midi_note = pretty_midi.Note(velocity=100, pitch=pitch, start=bar_start + 3.0 + i * note_duration, end=bar_start + 3.0 + i * note_duration + note_duration)
    piano.notes.append(midi_note)

# Bass: C (C2) to F (F2) with chromatic approach
bass_notes = [60, 61, 62, 62]
for i, pitch in enumerate(bass_notes):
    midi_note = pretty_midi.Note(velocity=100, pitch=pitch, start=bar_start + 3.0 + i * note_duration, end=bar_start + 3.0 + i * note_duration + note_duration)
    bass.notes.append(midi_note)

# Sax: A - D - F - A (finish the motif)
sax_notes = [67, 62, 64, 67]
for i, pitch in enumerate(sax_notes):
    midi_note = pretty_midi.Note(velocity=100, pitch=pitch, start=bar_start + 3.0 + i * note_duration, end=bar_start + 3.0 + i * note_duration + note_duration)
    sax.notes.append(midi_note)

# Add the drum pattern for bars 2-4
for bar in range(2, 4):
    bar_start = bar * 1.5
    for note in [36, 38, 42]:
        if note == 36:  # Kick
            midi_time = bar_start + 0.0
            midi_note = pretty_midi.Note(velocity=100, pitch=note, start=midi_time, end=midi_time + 0.375)
            drums.notes.append(midi_note)
            midi_time = bar_start + 0.75
            midi_note = pretty_midi.Note(velocity=100, pitch=note, start=midi_time, end=midi_time + 0.375)
            drums.notes.append(midi_note)
        elif note == 38:  # Snare
            midi_time = bar_start + 0.375
            midi_note = pretty_midi.Note(velocity=100, pitch=note, start=midi_time, end=midi_time + 0.375)
            drums.notes.append(midi_note)
            midi_time = bar_start + 1.125
            midi_note = pretty_midi.Note(velocity=100, pitch=note, start=midi_time, end=midi_time + 0.375)
            drums.notes.append(midi_note)
        elif note == 42:  # Hihat
            for i in range(4):
                midi_time = bar_start + i * 0.375
                midi_note = pretty_midi.Note(velocity=100, pitch=note, start=midi_time, end=midi_time + 0.125)
                drums.notes.append(midi_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
