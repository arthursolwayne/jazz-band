
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
bar1_start = 0.0
bar1_end = 1.5
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i, note in enumerate(kick_notes):
    note_time = bar1_start + (i * 0.75)
    kick = pretty_midi.Note(velocity=100, pitch=note, start=note_time, end=note_time + 0.375)
    drums.notes.append(kick)

for i, note in enumerate(snare_notes):
    note_time = bar1_start + (i * 0.75) + 0.1875
    snare = pretty_midi.Note(velocity=110, pitch=note, start=note_time, end=note_time + 0.375)
    drums.notes.append(snare)

for i, note in enumerate(hihat_notes):
    note_time = bar1_start + (i * 0.375)
    hihat = pretty_midi.Note(velocity=80, pitch=note, start=note_time, end=note_time + 0.1875)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)
bar_start = 1.5

# Marcus: Walking bass line in F (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (D2, MIDI 38), F (G2, MIDI 43), chromatic approach (E2, MIDI 37), F (D2, MIDI 38)
    38, 43, 37, 38,
    # Bar 3: C (A2, MIDI 45), C (E3, MIDI 50), chromatic approach (D#2, MIDI 44), C (A2, MIDI 45)
    45, 50, 44, 45,
    # Bar 4: G (D3, MIDI 51), G (A3, MIDI 56), chromatic approach (F#3, MIDI 55), G (D3, MIDI 51)
    51, 56, 55, 51
]
for i, note in enumerate(bass_notes):
    note_time = bar_start + (i * 0.375)
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=note_time, end=note_time + 0.375)
    bass.notes.append(bass_note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    # Bar 2: F (MIDI 65), A (MIDI 69), C (MIDI 60), E (MIDI 64)
    65, 69, 60, 64,
    # Bar 3: C7 (C, E, G, Bb)
    60, 64, 67, 62,
    # Bar 4: Gm7 (G, Bb, D, F)
    67, 62, 65, 60
]
for i, note in enumerate(piano_notes):
    note_time = bar_start + (i * 0.375)
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=note_time, end=note_time + 0.375)
    piano.notes.append(piano_note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start_time = bar_start + (bar - 2) * 1.5
    kick_notes = [36, 36]
    snare_notes = [38, 38]
    hihat_notes = [42] * 8

    for i, note in enumerate(kick_notes):
        note_time = bar_start_time + (i * 0.75)
        kick = pretty_midi.Note(velocity=100, pitch=note, start=note_time, end=note_time + 0.375)
        drums.notes.append(kick)

    for i, note in enumerate(snare_notes):
        note_time = bar_start_time + (i * 0.75) + 0.1875
        snare = pretty_midi.Note(velocity=110, pitch=note, start=note_time, end=note_time + 0.375)
        drums.notes.append(snare)

    for i, note in enumerate(hihat_notes):
        note_time = bar_start_time + (i * 0.375)
        hihat = pretty_midi.Note(velocity=80, pitch=note, start=note_time, end=note_time + 0.1875)
        drums.notes.append(hihat)

# You: Saxophone motif - short, singable, starts on F (MIDI 65), ends on C (MIDI 60)
# Motif: F (65), A (69), E (64), C (60)
sax_notes = [
    # Bar 2: F (65)
    65,
    # Bar 3: A (69)
    69,
    # Bar 4: E (64)
    64,
    # Bar 4: C (60)
    60
]
for i, note in enumerate(sax_notes):
    note_time = bar_start + (i * 0.375)
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=note_time, end=note_time + 0.375)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
