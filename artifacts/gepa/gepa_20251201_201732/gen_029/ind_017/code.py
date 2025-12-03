
import pretty_midi

# Initialize the MIDI file with the tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Time constants
bar_length = 1.5  # 1.5 seconds per bar at 160 BPM
beat_length = bar_length / 4  # 0.375 seconds per beat

# ----------------------------------
# Bar 1: Drums Only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
# Build tension, lay the foundation

for i in range(4):
    time = i * beat_length
    if i % 2 == 0:
        # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + 0.1)
        drums.notes.append(note)
    else:
        # Snare on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time, end=time + 0.1)
        drums.notes.append(note)
    
    # Hihat on every 8th note
    note = pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=time, end=time + 0.05)
    drums.notes.append(note)

# ----------------------------------
# Bar 2: Full Quartet (1.5 - 3.0s)
# Dm7 chord (D F A C) – Diane plays open voicings, one chord per bar
# Marcus: Walking bass line, D2-G2, roots and fifths with chromatic approaches
# Little Ray: Keep the same pattern, but now with the full band
# Dante: A short motif – start it, leave it hanging, come back to finish

# Diane's chord (Bar 2: Dm7)
chord_notes = [pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.5 + 0.5),  # D
               pretty_midi.Note(velocity=85, pitch=76, start=1.5, end=1.5 + 0.5),  # F
               pretty_midi.Note(velocity=85, pitch=79, start=1.5, end=1.5 + 0.5),  # A
               pretty_midi.Note(velocity=85, pitch=81, start=1.5, end=1.5 + 0.5)]  # C
piano.notes.extend(chord_notes)

# Marcus's walking bass line in Dm (D2-G2, roots and fifths with chromatic approaches)
# D2 (D) - F2 (chromatic approach) - G2 (G) - F2 (chromatic approach) - D2 (D)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=62, start=1.5, end=1.5 + 0.25),  # D2
    pretty_midi.Note(velocity=70, pitch=63, start=1.5 + 0.25, end=1.5 + 0.5),  # F2
    pretty_midi.Note(velocity=70, pitch=65, start=1.5 + 0.5, end=1.5 + 0.75),  # G2
    pretty_midi.Note(velocity=70, pitch=63, start=1.5 + 0.75, end=1.5 + 1.0),  # F2
]
bass.notes.extend(bass_notes)

# Drums: continue pattern from Bar 1
for i in range(4):
    time = 1.5 + i * beat_length
    if i % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + 0.1)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time, end=time + 0.1)
        drums.notes.append(note)
    
    note = pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=time, end=time + 0.05)
    drums.notes.append(note)

# Dante's motif – start it, leave it hanging, come back to finish
# Motif: D (E) -> F (G) -> A (B) -> C (D) – a question, not an answer
# Play D at beat 1, then leave the rest for the next bar

# Bar 2, beat 1: D (E) – it's a half note, hanging
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.75)
sax.notes.append(note)

# Bar 3: Full Quartet (3.0 - 4.5s)
# Diane: Gm7 (G Bb D F) – open voicing, resolve on the last beat

chord_notes = [pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.0 + 0.5),  # G
               pretty_midi.Note(velocity=85, pitch=80, start=3.0, end=3.0 + 0.5),  # Bb
               pretty_midi.Note(velocity=85, pitch=82, start=3.0, end=3.0 + 0.5),  # D
               pretty_midi.Note(velocity=85, pitch=84, start=3.0, end=3.0 + 0.5)]  # F
piano.notes.extend(chord_notes)

# Marcus: Walking bass line in Gm (G2, Bb2, D2, F2 – roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=67, start=3.0, end=3.0 + 0.25),  # G2
    pretty_midi.Note(velocity=70, pitch=68, start=3.0 + 0.25, end=3.0 + 0.5),  # Bb2
    pretty_midi.Note(velocity=70, pitch=70, start=3.0 + 0.5, end=3.0 + 0.75),  # D2
    pretty_midi.Note(velocity=70, pitch=69, start=3.0 + 0.75, end=3.0 + 1.0),  # F2
]
bass.notes.extend(bass_notes)

# Drums: continue pattern
for i in range(4):
    time = 3.0 + i * beat_length
    if i % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + 0.1)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time, end=time + 0.1)
        drums.notes.append(note)
    
    note = pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=time, end=time + 0.05)
    drums.notes.append(note)

# Dante's motif continuation – finish it in bar 3
# Play F, A, C at beat 2, 3, and 4 to complete the question

note = pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5)  # F
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=68, start=3.5, end=3.75)  # A
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0)  # C
sax.notes.append(note)

# Bar 4: Full Quartet (4.5 - 6.0s)
# Diane: Cm7 (C Eb G Bb) – resolve the tension
chord_notes = [pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.5 + 0.5),  # C
               pretty_midi.Note(velocity=85, pitch=74, start=4.5, end=4.5 + 0.5),  # Eb
               pretty_midi.Note(velocity=85, pitch=77, start=4.5, end=4.5 + 0.5),  # G
               pretty_midi.Note(velocity=85, pitch=79, start=4.5, end=4.5 + 0.5)]  # Bb
piano.notes.extend(chord_notes)

# Marcus: Walking bass line in Cm (C2, Eb2, G2, Bb2 – roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=60, start=4.5, end=4.5 + 0.25),  # C2
    pretty_midi.Note(velocity=70, pitch=62, start=4.5 + 0.25, end=4.5 + 0.5),  # Eb2
    pretty_midi.Note(velocity=70, pitch=65, start=4.5 + 0.5, end=4.5 + 0.75),  # G2
    pretty_midi.Note(velocity=70, pitch=63, start=4.5 + 0.75, end=4.5 + 1.0),  # Bb2
]
bass.notes.extend(bass_notes)

# Drums: continue pattern
for i in range(4):
    time = 4.5 + i * beat_length
    if i % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + 0.1)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time, end=time + 0.1)
        drums.notes.append(note)
    
    note = pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=time, end=time + 0.05)
    drums.notes.append(note)

# Dante: A whisper, a resolution – one note, held for the last bar
note = pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0)  # C
sax.notes.append(note)

# Add all instruments to the MIDI file
midi.instruments = [sax, bass, piano, drums]

# Save the MIDI file
# midi.write disabled
