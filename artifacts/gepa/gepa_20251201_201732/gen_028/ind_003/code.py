
import pretty_midi
import numpy as np

# Set up MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program, is_drum=True)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Tempo is already set via initial_tempo=160

# Define time for each bar (6 seconds for 4 bars, 1.5 sec per bar)
bar_duration = 1.5
beat_duration = bar_duration / 4  # 0.375 seconds per beat

# --- DRUMS: Little Ray (Bar 1: 1 and 3) ---
# Bar 1: Kick on 1 and 3, hihat on every eighth
# 0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625 (eighths)
# Kick on 0.0 and 0.75 (1st and 3rd beats)

kick_note = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.05)
drums.notes.append(kick_note)
kick_note = pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=0.8)
drums.notes.append(kick_note)

# Hihat on every eighth
hihat_note = pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.03)
drums.notes.append(hihat_note)
hihat_note = pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.4)
drums.notes.append(hihat_note)
hihat_note = pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.78)
drums.notes.append(hihat_note)
hihat_note = pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.15)
drums.notes.append(hihat_note)
hihat_note = pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.53)
drums.notes.append(hihat_note)
hihat_note = pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=1.9)
drums.notes.append(hihat_note)
hihat_note = pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.28)
drums.notes.append(hihat_note)
hihat_note = pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.65)
drums.notes.append(hihat_note)

# --- BASS: Marcus (Bar 1: walking line in Fm) ---
# Fm → F, Ab, D, C, Eb, D, F, Ab
# Root and fifth with chromatic approaches
# Bar 1: 0.0 - 1.5
# Notes in MIDI: F (65), Ab (68), D (62), C (60), Eb (64), D (62), F (65), Ab (68)

bass_notes = [65, 68, 62, 60, 64, 62, 65, 68]
for i, note in enumerate(bass_notes):
    start = i * beat_duration
    end = start + 0.1
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    bass.notes.append(bass_note)

# --- PIANO: Diane (Bar 1: open voicings, no comp) ---
# Bar 1: pass
# Bars 2-4: comp on 2 and 4 with open voicings
# Comp on 2 and 4 (0.75 and 1.5, 2.25 and 3.0)

# Bar 2: Fm7 (F, Ab, C, Eb) → open voicing
# F: 65, Ab: 68, C: 60, Eb: 64
# Play all at once on beat 2 (0.75)
piano_note = pretty_midi.Note(velocity=100, pitch=65, start=0.75, end=0.77)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=68, start=0.75, end=0.77)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=60, start=0.75, end=0.77)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=64, start=0.75, end=0.77)
piano.notes.append(piano_note)

# Bar 3: Bb7 (Bb, D, F, Ab) → open voicing
# Bb: 62, D: 67, F: 65, Ab: 68
piano_note = pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.27)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.27)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.27)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.27)
piano.notes.append(piano_note)

# Bar 4: Eb7 (Eb, G, Bb, D) → open voicing
# Eb: 64, G: 67, Bb: 62, D: 67
piano_note = pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.02)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.02)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.02)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.02)
piano.notes.append(piano_note)

# --- SAX: You (Bar 1: pass; Bar 2: motif) ---
# Bar 2: Start motif (F, Eb, D, C) → represent the melody

# F (65) at start of bar (1.5)
sax_note = pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.6)
sax.notes.append(sax_note)

# Eb (64) at 1.5 + 0.375 = 1.875
sax_note = pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=1.975)
sax.notes.append(sax_note)

# D (62) at 1.5 + 0.75 = 2.25
sax_note = pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.35)
sax.notes.append(sax_note)

# C (60) at 1.5 + 1.125 = 2.625
sax_note = pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=2.725)
sax.notes.append(sax_note)

# --- Write MIDI file ---
pm.write("intro_for_wayne.mid")

print("MIDI file written: 'intro_for_wayne.mid'")
