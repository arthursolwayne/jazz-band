
import pretty_midi
import numpy as np

# Initialize the MIDI file
pm = pretty_midi.PrettyMidi(initial_tempo=160)
track_drum = pretty_midi.Instrument(program=10)  # Drums
track_bass = pretty_midi.Instrument(program=33)  # Double Bass
track_piano = pretty_midi.Instrument(program=0)  # Acoustic Piano
track_sax = pretty_midi.Instrument(program=64)  # Tenor Sax

# Define the time in seconds per bar (6 seconds for 4 bars at 160 BPM)
bar_length = 1.5  # 1.5 seconds per bar
beat_length = 0.375  # 0.375 seconds per beat

# Define the key: D minor (D, F, G, A, Bb, C, D)
# Scale degrees: 1 (D), 2 (E), 3 (F), 4 (G), 5 (A), 6 (Bb), 7 (C)
# We'll use Dm7 (D, F, A, C) as a starting point but will use chromatic and altered intervals for tension

# BAR 1 - DRUMS: Little Ray sets it up with a simple but dark groove
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in [0, 2]:
        kick = pretty_midi.Note(velocity=100, pitch=36, start=bar * bar_length + beat * beat_length, end=bar * bar_length + beat * beat_length + 0.15)
        track_drum.notes.append(kick)
    for beat in [1, 3]:
        snare = pretty_midi.Note(velocity=100, pitch=38, start=bar * bar_length + beat * beat_length, end=bar * bar_length + beat * beat_length + 0.15)
        track_drum.notes.append(snare)
    for eighth in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=bar * bar_length + eighth * beat_length / 2, end=bar * bar_length + eighth * beat_length / 2 + 0.05)
        track_drum.notes.append(hihat)

# BAR 2 - BASS: Marcus walks with chromatic approaches
# Dm7: D, F, A, C
# Root and fifth with chromatic approaches
bar = 1
times = [bar * bar_length + beat * beat_length for beat in range(4)]
notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=times[0], end=times[0] + 0.25),  # D (root)
    pretty_midi.Note(velocity=100, pitch=49, start=times[1], end=times[1] + 0.25),  # C (chromatic approach to D)
    pretty_midi.Note(velocity=100, pitch=52, start=times[2], end=times[2] + 0.25),  # F (fifth)
    pretty_midi.Note(velocity=100, pitch=53, start=times[3], end=times[3] + 0.25),  # G (chromatic approach to F)
]
for note in notes:
    track_bass.notes.append(note)

# BAR 2 - PIANO: Diane plays open voicings, resolving on the last chord
# Chromatic chord changes, open voicings, resolving on Dm7
bar = 1
times = [bar * bar_length + beat * beat_length for beat in range(4)]
chords = [
    pretty_midi.Note(velocity=100, pitch=62, start=times[0], end=times[0] + 0.75),  # Gm7 (G, Bb, D, F) - D as root
    pretty_midi.Note(velocity=100, pitch=60, start=times[0], end=times[0] + 0.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=times[0], end=times[0] + 0.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=times[0], end=times[0] + 0.75),  # F

    pretty_midi.Note(velocity=100, pitch=61, start=times[1], end=times[1] + 0.75),  # A7 (A, C#, E, G) - D as root?
    pretty_midi.Note(velocity=100, pitch=63, start=times[1], end=times[1] + 0.75),  # C#
    pretty_midi.Note(velocity=100, pitch=69, start=times[1], end=times[1] + 0.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=times[1], end=times[1] + 0.75),  # G

    pretty_midi.Note(velocity=100, pitch=60, start=times[2], end=times[2] + 0.75),  # F7 (F, A, C, E) - D as root?
    pretty_midi.Note(velocity=100, pitch=65, start=times[2], end=times[2] + 0.75),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=times[2], end=times[2] + 0.75),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=times[2], end=times[2] + 0.75),  # E

    pretty_midi.Note(velocity=100, pitch=50, start=times[3], end=times[3] + 0.75),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=times[3], end=times[3] + 0.75),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=times[3], end=times[3] + 0.75),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=times[3], end=times[3] + 0.75),  # C
]
for note in chords:
    track_piano.notes.append(note)

# BAR 2 - SAX: Start the motif — a short phrase, incomplete, haunting
bar = 1
times = [bar * bar_length + beat * beat_length for beat in range(4)]
# Motif: D (50), F (52), rest, A (57)
# Ends on A, unresolved
notes = [
    pretty_midi.Note(velocity=110, pitch=50, start=times[0], end=times[0] + 0.5),
    pretty_midi.Note(velocity=110, pitch=52, start=times[1], end=times[1] + 0.5),
    pretty_midi.Note(velocity=110, pitch=57, start=times[3], end=times[3] + 0.5),
]
for note in notes:
    track_sax.notes.append(note)

# BAR 3 - BASS: Marcus continues with tension
bar = 2
times = [bar * bar_length + beat * beat_length for beat in range(4)]
notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=times[0], end=times[0] + 0.25),  # G (chromatic approach to F)
    pretty_midi.Note(velocity=100, pitch=52, start=times[1], end=times[1] + 0.25),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=times[2], end=times[2] + 0.25),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=times[3], end=times[3] + 0.25),  # C (chromatic approach to D)
]
for note in notes:
    track_bass.notes.append(note)

# BAR 3 - PIANO: Diane continues with ambiguous, unresolved chords
bar = 2
times = [bar * bar_length + beat * beat_length for beat in range(4)]
chords = [
    pretty_midi.Note(velocity=100, pitch=60, start=times[0], end=times[0] + 0.75),  # F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=65, start=times[0], end=times[0] + 0.75),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=times[0], end=times[0] + 0.75),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=times[0], end=times[0] + 0.75),  # E

    pretty_midi.Note(velocity=100, pitch=61, start=times[1], end=times[1] + 0.75),  # A7 (A, C#, E, G)
    pretty_midi.Note(velocity=100, pitch=63, start=times[1], end=times[1] + 0.75),  # C#
    pretty_midi.Note(velocity=100, pitch=69, start=times[1], end=times[1] + 0.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=times[1], end=times[1] + 0.75),  # G

    pretty_midi.Note(velocity=100, pitch=60, start=times[2], end=times[2] + 0.75),  # F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=65, start=times[2], end=times[2] + 0.75),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=times[2], end=times[2] + 0.75),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=times[2], end=times[2] + 0.75),  # E

    pretty_midi.Note(velocity=100, pitch=50, start=times[3], end=times[3] + 0.75),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=times[3], end=times[3] + 0.75),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=times[3], end=times[3] + 0.75),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=times[3], end=times[3] + 0.75),  # C
]
for note in chords:
    track_piano.notes.append(note)

# BAR 3 - SAX: Continue the motif with tension and space
bar = 2
times = [bar * bar_length + beat * beat_length for beat in range(4)]
# Motif: A (57), rest, rest, rest — hangs on the unresolved tone
notes = [
    pretty_midi.Note(velocity=110, pitch=57, start=times[0], end=times[0] + 0.5),
]
for note in notes:
    track_sax.notes.append(note)

# BAR 4 - BASS: Marcus resolves
bar = 3
times = [bar * bar_length + beat * beat_length for beat in range(4)]
notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=times[0], end=times[0] + 0.25),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=times[1], end=times[1] + 0.25),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=times[2], end=times[2] + 0.25),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=times[3], end=times[3] + 0.25),  # C
]
for note in notes:
    track_bass.notes.append(note)

# BAR 4 - PIANO: Diane resolves on Dm7 with a dark, open voicing
bar = 3
times = [bar * bar_length + beat * beat_length for beat in range(4)]
chords = [
    pretty_midi.Note(velocity=100, pitch=50, start=times[0], end=times[0] + 0.75),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=times[0], end=times[0] + 0.75),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=times[0], end=times[0] + 0.75),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=times[0], end=times[0] + 0.75),  # C

    pretty_midi.Note(velocity=100, pitch=50, start=times[1], end=times[1] + 0.75),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=times[1], end=times[1] + 0.75),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=times[1], end=times[1] + 0.75),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=times[1], end=times[1] + 0.75),  # C

    pretty_midi.Note(velocity=100, pitch=50, start=times[2], end=times[2] + 0.75),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=times[2], end=times[2] + 0.75),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=times[2], end=times[2] + 0.75),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=times[2], end=times[2] + 0.75),  # C

    pretty_midi.Note(velocity=100, pitch=50, start=times[3], end=times[3] + 0.75),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=times[3], end=times[3] + 0.75),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=times[3], end=times[3] + 0.75),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=times[3], end=times[3] + 0.75),  # C
]
for note in chords:
    track_piano.notes.append(note)

# BAR 4 - SAX: D, F, A, C — resolves the motif, but leaves it open
bar = 3
times = [bar * bar_length + beat * beat_length for beat in range(4)]
notes = [
    pretty_midi.Note(velocity=110, pitch=50, start=times[0], end=times[0] + 0.5),
    pretty_midi.Note(velocity=110, pitch=52, start=times[1], end=times[1] + 0.5),
    pretty_midi.Note(velocity=110, pitch=57, start=times[2], end=times[2] + 0.5),
    pretty_midi.Note(velocity=110, pitch=60, start=times[3], end=times[3] + 0.5),
]
for note in notes:
    track_sax.notes.append(note)

# Add instruments to the MIDI file
pm.instruments = [track_drum, track_bass, track_piano, track_sax]

# Save the MIDI file
pm.write("dante_intro.mid")
