
import pretty_midi

# Initialize a PrettyMIDI object at 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set the key to F minor (Fm)
# Fm: F, Ab, Bb, C, Eb, F, G, Ab

# Create instruments
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')

sax = pretty_midi.Instrument(program=sax_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)

# Add instruments to the MIDI file
midi.instruments = [sax, bass, piano, drums]

# Define a time in seconds for each beat (160 BPM = 0.375 seconds per beat)
beat = 0.375
bar = beat * 4

# Bar 1: Drums only — build tension
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Define note values
kick_note = 36  # C2
snare_note = 38  # D2
hihat_note = 42  # F2

# Time for bar 1 (6.0 seconds total, but only first bar = 1.5s)
bar_1_start = 0.0
bar_1_end = bar

# Kick on beat 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick_note, start=bar_1_start + 0.0, end=bar_1_start + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick_note, start=bar_1_start + beat * 2, end=bar_1_start + beat * 2 + 0.1))

# Snare on beat 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare_note, start=bar_1_start + beat, end=bar_1_start + beat + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare_note, start=bar_1_start + beat * 3, end=bar_1_start + beat * 3 + 0.1))

# Hihat on every eighth note
for i in range(8):
    hihat_start = bar_1_start + i * beat / 2
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat_note, start=hihat_start, end=hihat_start + 0.05))

# Bar 2: All instruments in — sax takes the melody

# Saxophone: Motif — start with a phrase that lingers, like a memory
# Fm scale: F, G, Ab, Bb, C, Db, Eb
# Motif: F, Ab, Bb, C — with space
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=bar_1_end + 0.0, end=bar_1_end + 0.2),  # F5
    pretty_midi.Note(velocity=100, pitch=67, start=bar_1_end + 0.4, end=bar_1_end + 0.6),  # Ab4
    pretty_midi.Note(velocity=100, pitch=64, start=bar_1_end + 0.8, end=bar_1_end + 1.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=bar_1_end + 1.2, end=bar_1_end + 1.4),  # C5
]

sax.notes.extend(sax_notes)

# Bass: Walking line in Fm (D2-G2), roots and fifths with chromatic approaches
# Bar 2: Fm7 (F, Ab, Bb, D)
# Roots: F (D2), Ab (D2), Bb (D2), F (D2)

# Bass notes
# Bar 2: F, Gb (chromatic), Ab, Bb
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=38, start=bar_1_end + 0.0, end=bar_1_end + 0.3),  # F2
    pretty_midi.Note(velocity=70, pitch=37, start=bar_1_end + 0.3, end=bar_1_end + 0.6),  # Gb2
    pretty_midi.Note(velocity=70, pitch=40, start=bar_1_end + 0.6, end=bar_1_end + 0.9),  # Ab2
    pretty_midi.Note(velocity=70, pitch=41, start=bar_1_end + 0.9, end=bar_1_end + 1.2),  # Bb2
]

bass.notes.extend(bass_notes)

# Piano: Open voicings, chord on 2 and 4

# Bar 2 chord: Fm7 (F, Ab, Bb, D)
# Play on beat 2 and 4

# Fm7 open voicing: F, Bb, Ab, D (C4, E4, F4, G4)
# Start at beat 2
chord_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=bar_1_end + beat, end=bar_1_end + beat + 0.2),  # F4
    pretty_midi.Note(velocity=100, pitch=65, start=bar_1_end + beat, end=bar_1_end + beat + 0.2),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=bar_1_end + beat, end=bar_1_end + beat + 0.2),  # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=bar_1_end + beat, end=bar_1_end + beat + 0.2),  # D4
]

piano.notes.extend(chord_notes)

# Bar 3: All instruments — continue the motif

# Saxophone: Continue the motif with a twist
# Listen to the space, then repeat with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=bar_1_end + bar, end=bar_1_end + bar + 0.2),  # F5
    pretty_midi.Note(velocity=100, pitch=67, start=bar_1_end + bar + 0.4, end=bar_1_end + bar + 0.6),  # Ab4
    pretty_midi.Note(velocity=100, pitch=64, start=bar_1_end + bar + 0.8, end=bar_1_end + bar + 1.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=bar_1_end + bar + 1.2, end=bar_1_end + bar + 1.4),  # C5
]

sax.notes.extend(sax_notes)

# Bass: Walking line — next chord is Bb7 (Bb, D, F, Ab)
# Roots: Bb (D2), C (D2), D (D2), Bb (D2)
# Chromatic approaches: Bb, B, C, D
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=41, start=bar_1_end + bar, end=bar_1_end + bar + 0.3),  # Bb2
    pretty_midi.Note(velocity=70, pitch=42, start=bar_1_end + bar + 0.3, end=bar_1_end + bar + 0.6),  # B2
    pretty_midi.Note(velocity=70, pitch=43, start=bar_1_end + bar + 0.6, end=bar_1_end + bar + 0.9),  # C2
    pretty_midi.Note(velocity=70, pitch=41, start=bar_1_end + bar + 0.9, end=bar_1_end + bar + 1.2),  # Bb2
]

bass.notes.extend(bass_notes)

# Piano: Bar 3 chord — Bb7 (Bb, D, F, Ab)
# Open voicing: Bb, D, F, Ab (F4, A4, Bb4, C4)
# Play on beat 2 and 4
chord_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=bar_1_end + bar + beat, end=bar_1_end + bar + beat + 0.2),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=bar_1_end + bar + beat, end=bar_1_end + bar + beat + 0.2),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=bar_1_end + bar + beat, end=bar_1_end + bar + beat + 0.2),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=bar_1_end + bar + beat, end=bar_1_end + bar + beat + 0.2),  # Ab4
]

piano.notes.extend(chord_notes)

# Bar 4: All instruments — return to Fm, resolve

# Saxophone: Return to the original motif, but with a slight change — maybe the last note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=bar_1_end + 2 * bar, end=bar_1_end + 2 * bar + 0.2),  # F5
    pretty_midi.Note(velocity=100, pitch=67, start=bar_1_end + 2 * bar + 0.4, end=bar_1_end + 2 * bar + 0.6),  # Ab4
    pretty_midi.Note(velocity=100, pitch=64, start=bar_1_end + 2 * bar + 0.8, end=bar_1_end + 2 * bar + 1.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=bar_1_end + 2 * bar + 1.2, end=bar_1_end + 2 * bar + 1.4),  # F5 (resolution)
]

sax.notes.extend(sax_notes)

# Bass: Walking line — resolve back to Fm (F, Ab, Bb, D)
# Roots: F (D2), Ab (D2), Bb (D2), F (D2)
# Chromatic approaches: F, F#, G, Ab
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=38, start=bar_1_end + 2 * bar, end=bar_1_end + 2 * bar + 0.3),  # F2
    pretty_midi.Note(velocity=70, pitch=39, start=bar_1_end + 2 * bar + 0.3, end=bar_1_end + 2 * bar + 0.6),  # F#2
    pretty_midi.Note(velocity=70, pitch=40, start=bar_1_end + 2 * bar + 0.6, end=bar_1_end + 2 * bar + 0.9),  # G2
    pretty_midi.Note(velocity=70, pitch=40, start=bar_1_end + 2 * bar + 0.9, end=bar_1_end + 2 * bar + 1.2),  # Ab2
]

bass.notes.extend(bass_notes)

# Piano: Bar 4 chord — Fm7 (F, Ab, Bb, D)
# Open voicing: F, Bb, Ab, D (F4, Bb4, Ab4, D4)
# Play on beat 2 and 4
chord_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=bar_1_end + 2 * bar + beat, end=bar_1_end + 2 * bar + beat + 0.2),  # F4
    pretty_midi.Note(velocity=100, pitch=65, start=bar_1_end + 2 * bar + beat, end=bar_1_end + 2 * bar + beat + 0.2),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=bar_1_end + 2 * bar + beat, end=bar_1_end + 2 * bar + beat + 0.2),  # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=bar_1_end + 2 * bar + beat, end=bar_1_end + 2 * bar + beat + 0.2),  # D4
]

piano.notes.extend(chord_notes)

# Write the MIDI file
# midi.write disabled
