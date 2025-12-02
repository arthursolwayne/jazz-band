
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125,
               1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125,
               3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125,
               4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375]

drum_notes = []
for t in kick_times:
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125))
for t in snare_times:
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.125))
for t in hihat_times:
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.125))
drums.notes.extend(drum_notes)

# Bar 2: Sax enters with a motif
# C7 - E7 - G7 - Bb7 (chromatic approach to Bb)
# 1.5s to 2.0s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=74, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.5)
]
sax.notes.extend(sax_notes)

# Marcus: Walking bass line (C - Bb - B - C)
# 1.5s to 6.0s
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=59, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=61, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=61, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=59, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=61, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=63, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=61, start=5.75, end=6.0)
]
bass.notes.extend(bass_notes)

# Diane: Comping with 7th chords on 2 and 4
# C7 (2), F7 (4)
piano_notes = [
    # Bar 2: C7 on 2 (1.875s)
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),

    # Bar 3: F7 on 2 (2.875s)
    pretty_midi.Note(velocity=100, pitch=65, start=2.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=72, start=2.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=76, start=2.875, end=3.0),

    # Bar 4: C7 on 2 (3.875s)
    pretty_midi.Note(velocity=100, pitch=60, start=3.875, end=4.0),
    pretty_midi.Note(velocity=100, pitch=64, start=3.875, end=4.0),
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.0),
    pretty_midi.Note(velocity=100, pitch=71, start=3.875, end=4.0),

    # Bar 4: F7 on 4 (5.0s)
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.25)
]
piano.notes.extend(piano_notes)

# Bar 3: Sax repeats the motif, descending
# G7 - Bb7 - C7 - E7 (chromatic approach to C)
# 2.5s to 3.0s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=70, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=74, start=3.25, end=3.5)
]
sax.notes.extend(sax_notes)

# Bar 4: Sax resolves the motif, ascending
# C7 - E7 - G7 - Bb7 (chromatic approach to Bb)
# 3.5s to 4.0s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=76, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=70, start=4.25, end=4.5)
]
sax.notes.extend(sax_notes)

# Bar 4: Continue the motif
# 4.5s to 5.0s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=74, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.5)
]
sax.notes.extend(sax_notes)

# Bar 4: Final resolution
# 5.5s to 6.0s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=74, start=5.75, end=6.0),
    pretty_midi.Note(velocity=100, pitch=76, start=6.0, end=6.25),
    pretty_midi.Note(velocity=100, pitch=70, start=6.25, end=6.5)
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
