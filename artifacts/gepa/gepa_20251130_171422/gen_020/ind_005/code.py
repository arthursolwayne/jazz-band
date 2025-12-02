
import pretty_midi
from pretty_midi import Instrument, Note

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]
pm.tempos = [pretty_midi.TempoChange(tempo=160, time=0)]

# Define the key: F minor (F, Gb, Ab, Bb, Cb, Db, Eb)
# MIDI note numbers for F minor scale (C4 = 60)
F_MINOR_SCALE = [65, 66, 67, 68, 69, 70, 71]  # F, Gb, Ab, Bb, B, Db, Eb

# Bar duration in seconds
BAR_DURATION = 1.5
BEAT_DURATION = 0.375
NOTE_DURATION = 0.25  # quarter note

# Create instruments
drums = Instrument(program=12, is_drum=True)
piano = Instrument(program=0)
bass = Instrument(program=33)
sax = Instrument(program=64)

# --- DRUMS: Kick on 1, 3; Snare on 2, 4; Hihat on every eighth ---
for bar in range(4):
    for beat in range(4):
        time = bar * BAR_DURATION + beat * BEAT_DURATION
        if beat == 0 or beat == 2:
            drums.notes.append(Note(36, time, duration=0.1))  # kick
        if beat == 1 or beat == 3:
            drums.notes.append(Note(38, time, duration=0.1))  # snare
        for eighth in range(2):
            eighth_time = time + eighth * 0.1875
            drums.notes.append(Note(42, eighth_time, duration=0.01))  # hihat

# --- PIANO: 7th chords, comp on 2 and 4 ---
# Fm7: F, Ab, Bb, Db
# Bb7: Bb, Db, F, Ab
# Fm7 again on beat 4
chords = [
    (65, 68, 71, 67),  # Fm7 on beat 1
    (68, 71, 65, 67),  # Bb7 on beat 2
    (65, 68, 71, 67),  # Fm7 on beat 3
    (68, 71, 65, 67),  # Bb7 on beat 4
]

for bar in range(4):
    for beat in range(4):
        time = bar * BAR_DURATION + beat * BEAT_DURATION
        if beat == 1 or beat == 3:
            for note in chords[beat]:
                piano.notes.append(Note(note, time, duration=0.25))

# --- BASS: Walking line, chromatic approaches, no repeats ---
bass_line = [65, 66, 67, 68, 69, 70, 71, 72, 71, 70, 69, 68, 67, 66, 65, 64]
for i, note in enumerate(bass_line):
    time = i * BEAT_DURATION
    bass.notes.append(Note(note, time, duration=0.2))

# --- SAX: One short motif, memorable, leaves space ---
# Motif: F (65) -> Ab (68) -> Bb (71) -> rest on beat 4
sax_notes = [
    Note(65, 0, duration=0.25),
    Note(68, 0.5, duration=0.25),
    Note(71, 1.0, duration=0.25),
    Note(65, 1.5, duration=0.25),  # repeat start of motif
    Note(68, 1.75, duration=0.25),
    Note(71, 2.0, duration=0.25),
    Note(65, 2.5, duration=0.25),
    Note(68, 2.75, duration=0.25),
    Note(71, 3.0, duration=0.25)
]

# Add the notes to the sax instrument
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI file
pm.instruments = [drums, piano, bass, sax]

# Save the MIDI file
pm.write("jazz_intro_Fm.mid")
