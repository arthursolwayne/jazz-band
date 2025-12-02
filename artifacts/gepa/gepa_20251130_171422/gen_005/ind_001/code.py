
import pretty_midi

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0.0)]

# Define the tempo and time in seconds
BPM = 160
time_per_bar = 60 / BPM * 4  # 4/4 time
time_per_beat = time_per_bar / 4

# Create instruments
drums = pretty_midi.Instrument(program=10)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

pm.instruments = [drums, bass, piano, sax]

# -----------------------------
# Bar 1: Drums only (tension, setup)
# -----------------------------

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375))

# Hi-hat on every eighth note (varied velocity to avoid monotony)
hi_hat_notes = [60, 61, 60, 61, 60, 61, 60, 61]
for i, pitch in enumerate(hi_hat_notes):
    start = i * time_per_beat / 2
    end = start + time_per_beat / 2
    velocity = 80 + (i % 2) * 10  # slight variation
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=end))

# -----------------------------
# Bars 2–4: Full ensemble
# -----------------------------

# -----------------------------
# Bass: Walking line, chromatic, no repeats
# -----------------------------
# F major scale: F G A Bb C D E
# Chromatic walking line for 3 bars (12 beats)
chromatic_walk = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
for i, pitch in enumerate(chromatic_walk):
    start = (1 + i * 0.375)  # 0.375s per beat
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# -----------------------------
# Piano: 7th chords, comp on 2 and 4
# -----------------------------
# F7 = F, A, C, E♭
# C7 = C, E, G, B♭
# G7 = G, B, D, F
# D7 = D, F#, A, C
# Each chord for 1 beat
chords = [
    [53, 57, 59, 55],  # F7
    [59, 62, 65, 61],  # C7
    [61, 65, 67, 59],  # G7
    [62, 66, 69, 64],  # D7
]
for i, chord in enumerate(chords):
    start = 1.5 + i * time_per_beat
    end = start + time_per_beat
    for pitch in chord:
        piano.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=start, end=end))

# -----------------------------
# Sax: Motif — concise, emotional, melodic
# -----------------------------
# F, A, B♭, C — a simple, ascending motif that feels like a memory
sax_notes = [
    [53, 57, 58, 60],  # F, A, B♭, C
    [53, 50, 53, 57],  # F, G, F, A (chromatic approach)
    [58, 60, 58, 57],  # B♭, C, B♭, A (falling resolution)
    [53, 57, 53, 60],  # F, A, F, C (return to the motif)
]
for i, note_group in enumerate(sax_notes):
    for j, pitch in enumerate(note_group):
        start = 1.5 + i * time_per_beat + j * 0.375
        end = start + 0.1875  # short, punchy notes
        sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# -----------------------------
# Output the MIDI file
# -----------------------------
pm.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'.")
