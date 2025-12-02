
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [36, 36, 36, 36]
snare_notes = [38, 38, 38, 38]
hihat_notes = [42, 42, 42, 42, 42, 42, 42, 42]

for i in range(4):
    kick = pretty_midi.Note(velocity=100, pitch=kick_notes[i], start=i*0.375, end=(i+1)*0.375)
    drums.notes.append(kick)
for i in range(4):
    snare = pretty_midi.Note(velocity=110, pitch=snare_notes[i], start=i*0.375 + 0.1875, end=(i+1)*0.375 + 0.1875)
    drums.notes.append(snare)
for i in range(8):
    hihat = pretty_midi.Note(velocity=80, pitch=hihat_notes[i], start=i*0.1875, end=(i+1)*0.1875)
    drums.notes.append(hihat)

# Bar 2: Full quartet starts (1.5 - 3.0s)
# Bass: Walking line in C, chromatic approaches
bass_notes = [60, 61, 62, 63, 64, 63, 62, 61, 60, 61, 62, 63, 64, 63, 62, 61]
for i, note in enumerate(bass_notes):
    start_time = 1.5 + (i * 0.375)
    end_time = start_time + 0.375
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start_time, end=end_time)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    60, 64, 67, 69,  # C7 (C, E, G, B)
    # Bar 3
    62, 66, 69, 71,  # D7 (D, F#, A, C)
    # Bar 4
    65, 69, 72, 74   # G7 (G, B, D, F#)
]
for i, chord in enumerate(piano_notes):
    start_time = 1.5 + (i * 0.375)
    end_time = start_time + 0.375
    piano_note = pretty_midi.Note(velocity=100, pitch=chord, start=start_time, end=end_time)
    piano.notes.append(piano_note)

# Sax: Melody starts in bar 2, one short motif
sax_notes = [62, 64, 65, 67, 65, 64, 62]  # F, G, G#, Bb, G#, G, F
for i, note in enumerate(sax_notes):
    start_time = 1.5 + (i * 0.375)
    end_time = start_time + 0.375
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start_time, end=end_time)
    sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass continues walking line
bass_notes = [60, 61, 62, 63, 64, 63, 62, 61, 60, 61, 62, 63, 64, 63, 62, 61]
for i, note in enumerate(bass_notes):
    start_time = 3.0 + (i * 0.375)
    end_time = start_time + 0.375
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start_time, end=end_time)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3
    62, 66, 69, 71,  # D7 (D, F#, A, C)
    # Bar 4
    65, 69, 72, 74   # G7 (G, B, D, F#)
]
for i, chord in enumerate(piano_notes):
    start_time = 3.0 + (i * 0.375)
    end_time = start_time + 0.375
    piano_note = pretty_midi.Note(velocity=100, pitch=chord, start=start_time, end=end_time)
    piano.notes.append(piano_note)

# Sax continues melody
sax_notes = [62, 63, 64, 65, 64, 62, 60]  # F, F#, G, G#, G, F, E
for i, note in enumerate(sax_notes):
    start_time = 3.0 + (i * 0.375)
    end_time = start_time + 0.375
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start_time, end=end_time)
    sax.notes.append(sax_note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass continues walking line
bass_notes = [60, 61, 62, 63, 64, 63, 62, 61, 60, 61, 62, 63, 64, 63, 62, 61]
for i, note in enumerate(bass_notes):
    start_time = 4.5 + (i * 0.375)
    end_time = start_time + 0.375
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start_time, end=end_time)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4
    65, 69, 72, 74   # G7 (G, B, D, F#)
]
for i, chord in enumerate(piano_notes):
    start_time = 4.5 + (i * 0.375)
    end_time = start_time + 0.375
    piano_note = pretty_midi.Note(velocity=100, pitch=chord, start=start_time, end=end_time)
    piano.notes.append(piano_note)

# Sax finishes the motif
sax_notes = [60, 62, 64, 65, 64, 62, 60]  # E, F#, G, G#, G, F#, E
for i, note in enumerate(sax_notes):
    start_time = 4.5 + (i * 0.375)
    end_time = start_time + 0.375
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start_time, end=end_time)
    sax.notes.append(sax_note)

# Drums: continue same pattern in bars 2-4
kick_notes = [36, 36, 36, 36]
snare_notes = [38, 38, 38, 38]
hihat_notes = [42, 42, 42, 42, 42, 42, 42, 42]

for i in range(4):
    kick = pretty_midi.Note(velocity=100, pitch=kick_notes[i], start=1.5 + i*0.375, end=1.5 + (i+1)*0.375)
    drums.notes.append(kick)
for i in range(4):
    snare = pretty_midi.Note(velocity=110, pitch=snare_notes[i], start=1.5 + i*0.375 + 0.1875, end=1.5 + (i+1)*0.375 + 0.1875)
    drums.notes.append(snare)
for i in range(8):
    hihat = pretty_midi.Note(velocity=80, pitch=hihat_notes[i], start=1.5 + i*0.1875, end=1.5 + (i+1)*0.1875)
    drums.notes.append(hihat)

# Append instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
