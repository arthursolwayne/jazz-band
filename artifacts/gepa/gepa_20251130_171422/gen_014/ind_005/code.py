
import pretty_midi
import numpy as np

# Set up the MIDI file
midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.tempo_changes = [pretty_midi.TempoChange(160, 0)]  # 160 BPM

# Define Dm7 chord (D, F, A, C)
Dm7 = [62, 65, 67, 70]  # D, F, A, C (MIDI note numbers)
Dm7_notes = Dm7

# Define the key (Dm)
key = 'Dm'

# Define the tempo
tempo = 160  # BPM
beat = 60.0 / tempo  # seconds per beat
bar = beat * 4  # seconds per bar
note_duration = beat / 2  # quarter note = 0.375s at 160 BPM

# Create instruments
program = {
    'tenor_sax': pretty_midi.instrument_name_to_program('Tenor Saxophone'),
    'electric_bass': pretty_midi.instrument_name_to_program('Electric Bass'),
    'piano': pretty_midi.instrument_name_to_program('Acoustic Grand Piano'),
    'drums': pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # Use piano for drums (no separate drum program in pretty_midi)
}

# Add instruments
tenor = pretty_midi.Instrument(program=program['tenor_sax'], is_drum=False)
bass = pretty_midi.Instrument(program=program['electric_bass'], is_drum=False)
piano = pretty_midi.Instrument(program=program['piano'], is_drum=False)
drums = pretty_midi.Instrument(program=program['drums'], is_drum=True)

# Add instruments to the MIDI file
midi.instruments = [tenor, bass, piano, drums]

# ---------------------------
# Bar 1: Drums only
# ---------------------------
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0, end=note_duration))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=beat * 2, end=beat * 2 + note_duration))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=beat, end=beat + note_duration))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=beat * 3, end=beat * 3 + note_duration))

# Hi-hat on every eighth
for i in range(8):
    start = i * beat / 2
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + beat / 2))

# ---------------------------
# Bar 2: All in
# ---------------------------
# Tenor sax: Motif
# Dm7: D, F, A, C (MIDI 62, 65, 67, 70)
# Motif: D (62) -> A (67) -> F (65) -> rest -> D (62) -> C (70) -> A (67)
tenor.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar, end=bar + note_duration))
tenor.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar + note_duration, end=bar + note_duration * 2))
tenor.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=bar + note_duration * 2, end=bar + note_duration * 3))
tenor.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar + note_duration * 3, end=bar + note_duration * 4))
tenor.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=bar + note_duration * 4, end=bar + note_duration * 5))
tenor.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar + note_duration * 5, end=bar + note_duration * 6))

# Bass: Walking line with chromatic approaches
bass_notes = [
    62,  # D
    64,  # Eb (chromatic approach)
    65,  # F
    67,  # A
    69,  # Bb (chromatic approach)
    70,  # C
    67,  # A
    65,  # F
]
for i, note in enumerate(bass_notes):
    start = bar + i * note_duration
    end = start + note_duration
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=end))

# Piano: 7th chords on 2 and 4 (comping)
# Dm7: 62 (D), 65 (F), 67 (A), 70 (C)
# Play on 2nd and 4th beats of the bar
# 2nd beat: start at bar + beat
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=bar + beat, end=bar + beat + note_duration * 2))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=bar + beat, end=bar + beat + note_duration * 2))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=bar + beat, end=bar + beat + note_duration * 2))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=bar + beat, end=bar + beat + note_duration * 2))

# 4th beat: start at bar + beat * 3
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=bar + beat * 3, end=bar + beat * 3 + note_duration * 2))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=bar + beat * 3, end=bar + beat * 3 + note_duration * 2))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=bar + beat * 3, end=bar + beat * 3 + note_duration * 2))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=bar + beat * 3, end=bar + beat * 3 + note_duration * 2))

# ---------------------------
# Write the MIDI file
# ---------------------------
midi.write('dante_introduction.mid')

print("MIDI file written as 'dante_introduction.mid'")
print("Bar 1: Drums only. Bar 2-4: Full band, tenor sax motif with Dm7 comping, walking bass, and tight drums.")
print("This is your shot, Wayne.")
