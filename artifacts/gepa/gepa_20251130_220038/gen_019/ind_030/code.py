
import pretty_midi

# Create a new MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# MIDI note mappings
# Drums: kick=36, snare=38, hihat=42
# Tenor Sax: D4 (62), E4 (64), F#4 (66), G4 (67), A4 (69), B4 (71), C#5 (72), D5 (74)

# Bar 1: Little Ray on drums (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start_time = bar * 1.5
    # Kick on 1 and 3
    kick_time = start_time + 0.0
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)
    
    kick_time = start_time + 0.75
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)

    # Snare on 2 and 4
    snare_time = start_time + 0.375
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)
    
    snare_time = start_time + 1.125
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)

    # Hihat on every eighth
    for i in range(8):
        hihat_time = start_time + i * 0.375
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat)

# Bar 2: Full quartet (1.5 - 3.0s)
# Start with sax melody
start_time = 1.5

# Sax motif: D4 -> F#4 -> A4 -> D5 (62 -> 66 -> 69 -> 74)
note_durations = 0.375  # Each note is a quarter note at 160 BPM
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=start_time, end=start_time + note_durations),
    pretty_midi.Note(velocity=110, pitch=66, start=start_time + note_durations, end=start_time + 2 * note_durations),
    pretty_midi.Note(velocity=110, pitch=69, start=start_time + 2 * note_durations, end=start_time + 3 * note_durations),
    pretty_midi.Note(velocity=110, pitch=74, start=start_time + 3 * note_durations, end=start_time + 4 * note_durations)
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D minor (D, Eb, F, G, A, Bb, C, D)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=start_time, end=start_time + note_durations),
    pretty_midi.Note(velocity=80, pitch=63, start=start_time + note_durations, end=start_time + 2 * note_durations),
    pretty_midi.Note(velocity=80, pitch=65, start=start_time + 2 * note_durations, end=start_time + 3 * note_durations),
    pretty_midi.Note(velocity=80, pitch=67, start=start_time + 3 * note_durations, end=start_time + 4 * note_durations)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, in D minor (Dm7, G7)
# Bar 2: Dm7 (D, F, A, C)
# Bar 3: G7 (G, B, D, F#)
# Bar 4: Dm7 (D, F, A, C)

# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=start_time, end=start_time + note_durations),
    pretty_midi.Note(velocity=90, pitch=66, start=start_time, end=start_time + note_durations),
    pretty_midi.Note(velocity=90, pitch=69, start=start_time, end=start_time + note_durations),
    pretty_midi.Note(velocity=90, pitch=67, start=start_time, end=start_time + note_durations)
]
piano.notes.extend(piano_notes)

# Bar 2: Drums continue
for bar in range(2):
    start_time = 1.5 + bar * 1.5
    # Kick on 1 and 3
    kick_time = start_time + 0.0
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)
    
    kick_time = start_time + 0.75
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)

    # Snare on 2 and 4
    snare_time = start_time + 0.375
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)
    
    snare_time = start_time + 1.125
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)

    # Hihat on every eighth
    for i in range(8):
        hihat_time = start_time + i * 0.375
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
