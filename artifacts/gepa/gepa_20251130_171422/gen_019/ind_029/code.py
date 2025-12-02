
import pretty_midi
import numpy as np

# Setup
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0.0)]

# Define time increments for 160 BPM, 4/4 time
bpm = 160
notes_per_beat = 4
beat_time = 60.0 / bpm  # seconds per beat
bar_time = beat_time * 4  # seconds per bar

# Create instruments
tenor_sax = pretty_midi.Instrument(program=64)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
drums = pretty_midi.Instrument(program=0, is_drum=True)

pm.instruments = [tenor_sax, bass, piano, drums]

# --- Drums: Little Ray's groove (Bar 1 only) ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

for bar in range(1):
    for beat in range(4):
        time = bar * bar_time + beat * beat_time
        if beat == 0 or beat == 2:
            # Kick
            note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            # Snare
            note = pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time, end=time + 0.1)
            drums.notes.append(note)
        # Hihat on every eighth
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=time + eighth * beat_time / 2, end=time + eighth * beat_time / 2 + 0.05)
            drums.notes.append(note)

# --- Bass: Marcus's walking line (Bars 1-4) ---
# Start on D (2nd octave)
bass_root = 62  # D4

# Walking line with chromatic approaches
bass_notes = [
    (62, 0.0),  # D4
    (63, 0.5),  # D#4
    (62, 1.0),  # D4
    (64, 1.5),  # E4
    (62, 2.0),  # D4
    (63, 2.5),  # D#4
    (62, 3.0),  # D4
    (64, 3.5),  # E4
    (62, 4.0),  # D4
    (63, 4.5),  # D#4
    (62, 5.0),  # D4
    (64, 5.5),  # E4
    (62, 6.0),  # D4
    (63, 6.5),  # D#4
    (62, 7.0),  # D4
    (64, 7.5),  # E4
]

for pitch, time in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.1)
    bass.notes.append(note)

# --- Piano: Diane's comping (Bars 1-4) ---
# 7th chords on 2 and 4
diane_chords = [
    (76, 0.5),  # A7 (76 = A4)
    (74, 1.5),  # G7 (74 = G4)
    (76, 2.5),  # A7
    (74, 3.5),  # G7
    (76, 4.5),  # A7
    (74, 5.5),  # G7
    (76, 6.5),  # A7
    (74, 7.5),  # G7
]

for pitch, time in diane_chords:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.1)
    piano.notes.append(note)

# --- Tenor Sax: Dante's melody (Bars 1-4) ---
# Melody: start with a strong note (D, 62), then a question (F#, 66), leave it hanging
# Then return in a new voice

# Bar 1: Start with D, then F#
tenor_notes = [
    (62, 0.0),  # D4
    (66, 0.5),  # F#4
    (62, 1.0),  # D4
    (62, 1.5),  # D4
    (64, 2.0),  # E4
    (62, 2.5),  # D4
    (60, 3.0),  # C4
    (62, 3.5),  # D4
    (64, 4.0),  # E4
    (62, 4.5),  # D4
    (66, 5.0),  # F#4
    (62, 5.5),  # D4
    (62, 6.0),  # D4
    (64, 6.5),  # E4
    (62, 7.0),  # D4
]

for pitch, time in tenor_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.1)
    tenor_sax.notes.append(note)

# Save the MIDI file
pm.write('wayne_intro.mid')
