
import pretty_midi
import numpy as np

# Constants
BPM = 160
BEAT = 60.0 / BPM  # seconds per beat
BAR_DURATION = 4 * BEAT  # 4/4 time
NOTE_DURATION = 0.1  # base note length
DYNAMIC_RANGE = (30, 90)  # MIDI velocity range (soft to loud)

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=BPM)

# Instrument assignment
drums = pretty_midi.Instrument(program=10)  # Drums (drum kit)
bass = pretty_midi.Instrument(program=33)   # Bass (acoustic bass)
piano = pretty_midi.Instrument(program=0)   # Piano
sax = pretty_midi.Instrument(program=66)    # Tenor Saxophone

pm.instruments = [drums, bass, piano, sax]

# --- BAR 1: Drums Only (Little Ray) ---
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=np.random.randint(*DYNAMIC_RANGE), pitch=36, start=0, end=0 + BEAT))
drums.notes.append(pretty_midi.Note(velocity=np.random.randint(*DYNAMIC_RANGE), pitch=36, start=2 * BEAT, end=2 * BEAT + BEAT))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=np.random.randint(*DYNAMIC_RANGE), pitch=38, start=1 * BEAT, end=1 * BEAT + BEAT))
drums.notes.append(pretty_midi.Note(velocity=np.random.randint(*DYNAMIC_RANGE), pitch=38, start=3 * BEAT, end=3 * BEAT + BEAT))

# Hi-hat on every eighth note
for i in range(8):
    start = i * BEAT / 2
    duration = BEAT / 2
    velocity = np.random.randint(*DYNAMIC_RANGE)
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=42, start=start, end=start + duration))

# --- BAR 2: Full Ensemble (Start of Melody) ---

# Tenor Saxophone - Motif begins
# Fm scale: F, Gb, Ab, Bb, B, Db, Eb
# Motif: F -> Ab -> B -> Eb (not a scale run, but a short, meaningful gesture)
sax_notes = [
    pretty_midi.Note(velocity=np.random.randint(*DYNAMIC_RANGE), pitch=65, start=0, end=0 + BEAT),
    pretty_midi.Note(velocity=np.random.randint(*DYNAMIC_RANGE), pitch=60, start=0.6 * BEAT, end=0.6 * BEAT + 0.2 * BEAT),
    pretty_midi.Note(velocity=np.random.randint(*DYNAMIC_RANGE), pitch=62, start=1.1 * BEAT, end=1.1 * BEAT + 0.2 * BEAT),
    pretty_midi.Note(velocity=np.random.randint(*DYNAMIC_RANGE), pitch=59, start=1.6 * BEAT, end=1.6 * BEAT + 0.2 * BEAT),
]

sax.notes.extend(sax_notes)

# Bass - Walking line in Fm (chromatic, no repeat notes)
bass_notes = [
    pretty_midi.Note(velocity=60, pitch=45, start=0, end=0 + BEAT),
    pretty_midi.Note(velocity=60, pitch=44, start=BEAT, end=BEAT + BEAT),
    pretty_midi.Note(velocity=60, pitch=46, start=2 * BEAT, end=2 * BEAT + BEAT),
    pretty_midi.Note(velocity=60, pitch=47, start=3 * BEAT, end=3 * BEAT + BEAT),
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 & 4 (comping)
# Fm7: F, Ab, Bb, Db
# Bb7: Bb, Db, Eb, F
piano_notes = [
    pretty_midi.Note(velocity=70, pitch=65, start=1 * BEAT, end=1 * BEAT + BEAT),  # F
    pretty_midi.Note(velocity=70, pitch=60, start=1 * BEAT, end=1 * BEAT + BEAT),  # Ab
    pretty_midi.Note(velocity=70, pitch=59, start=1 * BEAT, end=1 * BEAT + BEAT),  # Bb
    pretty_midi.Note(velocity=70, pitch=57, start=1 * BEAT, end=1 * BEAT + BEAT),  # Db

    pretty_midi.Note(velocity=70, pitch=59, start=3 * BEAT, end=3 * BEAT + BEAT),  # Bb
    pretty_midi.Note(velocity=70, pitch=57, start=3 * BEAT, end=3 * BEAT + BEAT),  # Db
    pretty_midi.Note(velocity=70, pitch=62, start=3 * BEAT, end=3 * BEAT + BEAT),  # Eb
    pretty_midi.Note(velocity=70, pitch=65, start=3 * BEAT, end=3 * BEAT + BEAT),  # F
]

piano.notes.extend(piano_notes)

# --- BAR 3 & 4: Continue the Motif, leave it hanging ---

# Saxophone - continue motif slightly differently
# F -> Ab -> B -> Eb (same motif but slightly delayed, with a rest at the end)
sax_notes = [
    pretty_midi.Note(velocity=np.random.randint(*DYNAMIC_RANGE), pitch=65, start=1 * BEAT, end=1 * BEAT + BEAT),
    pretty_midi.Note(velocity=np.random.randint(*DYNAMIC_RANGE), pitch=60, start=1.6 * BEAT, end=1.6 * BEAT + 0.2 * BEAT),
    pretty_midi.Note(velocity=np.random.randint(*DYNAMIC_RANGE), pitch=62, start=2.1 * BEAT, end=2.1 * BEAT + 0.2 * BEAT),
    pretty_midi.Note(velocity=np.random.randint(*DYNAMIC_RANGE), pitch=59, start=2.6 * BEAT, end=2.6 * BEAT + 0.2 * BEAT),
    # Leave the last note hanging
    pretty_midi.Note(velocity=np.random.randint(*DYNAMIC_RANGE), pitch=59, start=3.0 * BEAT, end=3.0 * BEAT + 0.2 * BEAT),
]
sax.notes.extend(sax_notes)

# Bass - continue walking line
bass_notes = [
    pretty_midi.Note(velocity=60, pitch=48, start=4 * BEAT, end=4 * BEAT + BEAT),
    pretty_midi.Note(velocity=60, pitch=49, start=5 * BEAT, end=5 * BEAT + BEAT),
    pretty_midi.Note(velocity=60, pitch=50, start=6 * BEAT, end=6 * BEAT + BEAT),
    pretty_midi.Note(velocity=60, pitch=51, start=7 * BEAT, end=7 * BEAT + BEAT),
]
bass.notes.extend(bass_notes)

# Piano - continue comping
piano_notes = [
    pretty_midi.Note(velocity=70, pitch=65, start=4 * BEAT, end=4 * BEAT + BEAT),  # F
    pretty_midi.Note(velocity=70, pitch=60, start=4 * BEAT, end=4 * BEAT + BEAT),  # Ab
    pretty_midi.Note(velocity=70, pitch=59, start=4 * BEAT, end=4 * BEAT + BEAT),  # Bb
    pretty_midi.Note(velocity=70, pitch=57, start=4 * BEAT, end=4 * BEAT + BEAT),  # Db

    pretty_midi.Note(velocity=70, pitch=59, start=6 * BEAT, end=6 * BEAT + BEAT),  # Bb
    pretty_midi.Note(velocity=70, pitch=57, start=6 * BEAT, end=6 * BEAT + BEAT),  # Db
    pretty_midi.Note(velocity=70, pitch=62, start=6 * BEAT, end=6 * BEAT + BEAT),  # Eb
    pretty_midi.Note(velocity=70, pitch=65, start=6 * BEAT, end=6 * BEAT + BEAT),  # F
]

piano.notes.extend(piano_notes)

# --- Drums continue in bar 3 and 4 with slight variations ---
# Kick
drums.notes.append(pretty_midi.Note(velocity=np.random.randint(*DYNAMIC_RANGE), pitch=36, start=4 * BEAT, end=4 * BEAT + BEAT))
drums.notes.append(pretty_midi.Note(velocity=np.random.randint(*DYNAMIC_RANGE), pitch=36, start=6 * BEAT, end=6 * BEAT + BEAT))

# Snare
drums.notes.append(pretty_midi.Note(velocity=np.random.randint(*DYNAMIC_RANGE), pitch=38, start=5 * BEAT, end=5 * BEAT + BEAT))
drums.notes.append(pretty_midi.Note(velocity=np.random.randint(*DYNAMIC_RANGE), pitch=38, start=7 * BEAT, end=7 * BEAT + BEAT))

# Hi-hats with slight variation
for i in range(8):
    start = i * BEAT / 2
    duration = BEAT / 2
    velocity = np.random.randint(*DYNAMIC_RANGE)
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=42, start=start + 2 * BEAT, end=start + 2 * BEAT + duration))

# Write the MIDI file
pm.write("jazz_intro.mid")

print("MIDI file 'jazz_intro.mid' created.")
