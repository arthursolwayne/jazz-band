
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
bar_length = 1.5
for bar in range(1):
    start = bar * bar_length
    # Kick on 1 and 3
    kick_time = start + 0.0
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.05)
    drums.notes.append(kick)
    kick_time = start + 0.75
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.05)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare_time = start + 0.375
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.05)
    drums.notes.append(snare)
    snare_time = start + 1.125
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.05)
    drums.notes.append(snare)
    # Hi-hat on every eighth
    for i in range(8):
        hihat_time = start + i * 0.375
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2
start = 1.5
bass_notes = [38, 40, 43, 38, 40, 42, 43, 38]  # D2, F2, A2, D2, F2, G2, A2, D2
for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + 0.25)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on last
# Bar 2: D7sus4 (D, G, B, F#)
piano_notes = [62, 67, 71, 67]
for i, pitch in enumerate(piano_notes):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + 0.25)
    piano.notes.append(note)

# Bar 3: G7 (G, B, D, F#)
piano_notes = [67, 71, 74, 67]
for i, pitch in enumerate(piano_notes):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + 1.5 + i * 0.375, end=start + 1.5 + i * 0.375 + 0.25)
    piano.notes.append(note)

# Bar 4: C7 (C, E, G, B)
piano_notes = [60, 64, 67, 71]
for i, pitch in enumerate(piano_notes):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + 3.0 + i * 0.375, end=start + 3.0 + i * 0.375 + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing, start it, leave it hanging, come back and finish it
# Motif: D (62), F# (66), G (67), D (62)
# Play first two notes in bar 2, leave the last two for bar 4
# Bar 2
note = pretty_midi.Note(velocity=110, pitch=62, start=start, end=start + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=66, start=start + 0.375, end=start + 0.625)
sax.notes.append(note)

# Bar 4
note = pretty_midi.Note(velocity=110, pitch=67, start=start + 3.0, end=start + 3.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=62, start=start + 3.375, end=start + 3.75)
sax.notes.append(note)

# Drums: Bar 2-4
for bar in range(2, 4):
    start = bar * bar_length
    # Kick on 1 and 3
    kick_time = start + 0.0
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.05)
    drums.notes.append(kick)
    kick_time = start + 0.75
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.05)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare_time = start + 0.375
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.05)
    drums.notes.append(snare)
    snare_time = start + 1.125
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.05)
    drums.notes.append(snare)
    # Hi-hat on every eighth
    for i in range(8):
        hihat_time = start + i * 0.375
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
