
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Bar duration in seconds = 1.5s (160 BPM, 4/4 time)
bar_duration = 1.5
beat_duration = 0.375

# Bar 1: Little Ray alone (0.0 - 1.5s) — Drums only
# Kick on 1 and 3, Snare on 2 and 4, Hi-Hat on every 8th
for i in range(0, 2):  # Two beats per bar
    kick = pretty_midi.Note(velocity=100, pitch=KICK, start=(i * beat_duration), end=(i * beat_duration) + beat_duration)
    snare = pretty_midi.Note(velocity=100, pitch=SNARE, start=(i * beat_duration) + beat_duration, end=(i * beat_duration) + 2 * beat_duration)
    for j in range(0, 2):  # Hi-Hat every 8th note
        hihat = pretty_midi.Note(velocity=80, pitch=HIHAT, start=(i * beat_duration) + j * beat_duration / 2, end=(i * beat_duration) + j * beat_duration / 2 + beat_duration / 2)
        drums.notes.append(hihat)
    drums.notes.append(kick)
    drums.notes.append(snare)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Saxophone motif — Dm7 -> F -> G -> C (Dm, F, G, C)
# Start with Dm7 (D, F, A, C) and play a short motif: D -> F -> G -> C (melodic minor interval)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=1.625, end=1.75), # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875), # G
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.0),  # C
]
sax.notes.extend(sax_notes)

# Bass line: Chromatic walking line from Dm7 (D, F, A, C)
# D -> Eb -> F -> G -> A -> Bb -> B -> C -> D (chromatic walking line)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),    # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.75, end=2.0),    # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.25),    # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),    # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),    # A
    pretty_midi.Note(velocity=90, pitch=70, start=2.75, end=3.0),    # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),    # B
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),    # C
]
bass.notes.extend(bass_notes)

# Piano: Dm7 chords on beat 2 and 4
# Dm7 = D, F, A, C
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.75),  # C
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-4 — Kick on 1 and 3, Snare on 2 and 4, Hi-Hat on every 8th
for bar in range(2, 4):  # Bars 2 and 3
    start = bar * bar_duration
    for i in range(0, 2):  # Two beats per bar
        kick = pretty_midi.Note(velocity=100, pitch=KICK, start=start + i * beat_duration, end=start + i * beat_duration + beat_duration)
        snare = pretty_midi.Note(velocity=100, pitch=SNARE, start=start + i * beat_duration + beat_duration, end=start + i * beat_duration + 2 * beat_duration)
        for j in range(0, 2):  # Hi-Hat every 8th note
            hihat = pretty_midi.Note(velocity=80, pitch=HIHAT, start=start + i * beat_duration + j * beat_duration / 2, end=start + i * beat_duration + j * beat_duration / 2 + beat_duration / 2)
            drums.notes.append(hihat)
        drums.notes.append(kick)
        drums.notes.append(snare)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_intro.mid')
