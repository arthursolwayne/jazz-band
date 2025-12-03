
import pretty_midi
from pretty_midi import Note, Instrument

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Create instruments
bass = Instrument(program=33, is_drum=False, name="Bass")
piano = Instrument(program=0, is_drum=False, name="Piano")
drums = Instrument(program=0, is_drum=True, name="Drums")
sax = Instrument(program=64, is_drum=False, name="Saxophone")

pm.instruments = [bass, piano, drums, sax]

# Define the key: F minor (F, Gb, Ab, Bb, B, Db, Eb)
# We'll use this to build chord tones and melodic ideas

# Define time in seconds per bar
BPM = 160
beats_per_bar = 4
seconds_per_beat = 60.0 / BPM
seconds_per_bar = seconds_per_beat * beats_per_bar  # 6.0 seconds for 4 bars

# Function to convert bar + beat to time
def bar_beat_to_time(bar, beat):
    return (bar * beats_per_bar + beat) * seconds_per_beat

# ====================
# DRUMS (Little Ray)
# ====================

# Hi-hat on every eighth note
for beat in range(0, 4 * 2):  # 4 bars, 2 beats per bar (8th notes)
    time = bar_beat_to_time(beat // 2, beat % 2)
    hi_hat = Note(velocity=100, start=time, end=time + 0.05)
    hi_hat.pitch = 42  # Hi-hat
    drums.notes.append(hi_hat)

# Kick on 1 and 3 of each bar
for bar in range(4):
    kick_time = bar_beat_to_time(bar, 0)
    kick = Note(velocity=110, start=kick_time, end=kick_time + 0.1)
    kick.pitch = 36  # Kick
    drums.notes.append(kick)
    kick_time = bar_beat_to_time(bar, 2)
    kick = Note(velocity=110, start=kick_time, end=kick_time + 0.1)
    kick.pitch = 36
    drums.notes.append(kick)

# Snare on 2 and 4 of each bar
for bar in range(4):
    snare_time = bar_beat_to_time(bar, 1)
    snare = Note(velocity=105, start=snare_time, end=snare_time + 0.1)
    snare.pitch = 38  # Snare
    drums.notes.append(snare)
    snare_time = bar_beat_to_time(bar, 3)
    snare = Note(velocity=105, start=snare_time, end=snare_time + 0.1)
    snare.pitch = 38
    drums.notes.append(snare)

# ====================
# BASS (Marcus)
# ====================

# Walking line in Fm: F - Gb - Ab - Bb - B - Db - Eb (chromatic approaches)
# Root and fifth with chromatic approaches
# Bar 1: F (root), Gb (chromatic), Ab (fifth), Bb (chromatic)
# Bar 2: B (chromatic), Db (fifth), Eb (chromatic), F (root)
# Bar 3: Gb (chromatic), Ab (fifth), Bb (chromatic), B (chromatic)
# Bar 4: Db (fifth), Eb (chromatic), F (root), Gb (chromatic)

bass_notes = [
    # Bar 1
    Note(velocity=100, start=0, end=0.375, pitch=48),  # F2
    Note(velocity=100, start=0.375, end=0.75, pitch=47), # Gb2
    Note(velocity=100, start=0.75, end=1.125, pitch=50), # Ab2
    Note(velocity=100, start=1.125, end=1.5, pitch=51),  # Bb2

    # Bar 2
    Note(velocity=100, start=1.5, end=1.875, pitch=53),  # B2
    Note(velocity=100, start=1.875, end=2.25, pitch=50),  # Ab2 (fifth)
    Note(velocity=100, start=2.25, end=2.625, pitch=52),  # Bb2 (chromatic)
    Note(velocity=100, start=2.625, end=3.0, pitch=48),   # F2 (root)

    # Bar 3
    Note(velocity=100, start=3.0, end=3.375, pitch=47),   # Gb2 (chromatic)
    Note(velocity=100, start=3.375, end=3.75, pitch=50),  # Ab2 (fifth)
    Note(velocity=100, start=3.75, end=4.125, pitch=51),  # Bb2 (chromatic)
    Note(velocity=100, start=4.125, end=4.5, pitch=53),   # B2 (chromatic)

    # Bar 4
    Note(velocity=100, start=4.5, end=4.875, pitch=50),   # Ab2 (fifth)
    Note(velocity=100, start=4.875, end=5.25, pitch=52),  # Bb2 (chromatic)
    Note(velocity=100, start=5.25, end=5.625, pitch=48),  # F2 (root)
    Note(velocity=100, start=5.625, end=6.0, pitch=47),   # Gb2 (chromatic)
]

for note in bass_notes:
    bass.notes.append(note)

# ====================
# PIANO (Diane)
# ====================

# Open voicings, different chords each bar, resolving on the last beat

# Bar 1: Fm7 (F, Ab, Bb, Db)
# Bar 2: Gb7 (Gb, Bb, Db, F)
# Bar 3: Ab7 (Ab, C, Eb, Gb)
# Bar 4: Bb7 (Bb, D, F, Ab)

chords = [
    # Bar 1: Fm7
    # F (48), Ab (50), Bb (51), Db (53)
    Note(velocity=100, start=0, end=0.375, pitch=48),
    Note(velocity=100, start=0, end=0.375, pitch=50),
    Note(velocity=100, start=0, end=0.375, pitch=51),
    Note(velocity=100, start=0, end=0.375, pitch=53),

    # Bar 2: Gb7
    Note(velocity=100, start=1.5, end=1.875, pitch=47),
    Note(velocity=100, start=1.5, end=1.875, pitch=51),
    Note(velocity=100, start=1.5, end=1.875, pitch=53),
    Note(velocity=100, start=1.5, end=1.875, pitch=48),

    # Bar 3: Ab7
    Note(velocity=100, start=3.0, end=3.375, pitch=50),
    Note(velocity=100, start=3.0, end=3.375, pitch=52),
    Note(velocity=100, start=3.0, end=3.375, pitch=55),
    Note(velocity=100, start=3.0, end=3.375, pitch=47),

    # Bar 4: Bb7
    Note(velocity=100, start=4.5, end=4.875, pitch=51),
    Note(velocity=100, start=4.5, end=4.875, pitch=54),
    Note(velocity=100, start=4.5, end=4.875, pitch=48),
    Note(velocity=100, start=4.5, end=4.875, pitch=50),
]

for note in chords:
    piano.notes.append(note)

# ====================
# SAX (You)
# ====================

# A short motif that *yearns* — a phrase that starts, leaves it hanging, and returns.
# F - Ab (chromatic) - Bb (fifth) - F (root)
# Start on beat 1, end before the end of bar 4

sax_notes = [
    Note(velocity=110, start=0, end=0.5, pitch=48),   # F2
    Note(velocity=110, start=0.5, end=0.75, pitch=50), # Ab2
    Note(velocity=110, start=0.75, end=1.25, pitch=51), # Bb2
    Note(velocity=110, start=1.25, end=1.5, pitch=48), # F2 (end of bar 1)

    # Silence in bar 2
    # Silence in bar 3
    # Then the *shout* in bar 4

    Note(velocity=110, start=4.5, end=5.5, pitch=48),   # F2 again, but longer, more emotional
    Note(velocity=110, start=5.5, end=5.75, pitch=50), # Ab2
    Note(velocity=110, start=5.75, end=6.0, pitch=51)  # Bb2
]

for note in sax_notes:
    sax.notes.append(note)

# Write the MIDI file
pm.write("jazz_intro.mid")
