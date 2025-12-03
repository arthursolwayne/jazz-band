
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = []
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 2 and 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))
    # Hihat on every eighth
    for i in range(8):
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: D2-G2, roots and fifths with chromatic approaches
bass_notes = []
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=38, start=start + 0.0, end=start + 0.375))  # D2
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=40, start=start + 0.375, end=start + 0.75))  # Eb2 (chromatic)
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=43, start=start + 0.75, end=start + 1.125))  # G2
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=41, start=start + 1.125, end=start + 1.5))  # F2 (chromatic)
    elif bar == 3:
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=43, start=start + 0.0, end=start + 0.375))  # G2
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=45, start=start + 0.375, end=start + 0.75))  # A2
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=48, start=start + 0.75, end=start + 1.125))  # C3
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=46, start=start + 1.125, end=start + 1.5))  # Bb2 (chromatic)
    elif bar == 4:
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=48, start=start + 0.0, end=start + 0.375))  # C3
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=50, start=start + 0.375, end=start + 0.75))  # D3
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=53, start=start + 0.75, end=start + 1.125))  # F3
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=51, start=start + 1.125, end=start + 1.5))  # Eb3 (chromatic)

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = []
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Dmaj7 (D F# A C#)
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=50, start=start + 0.0, end=start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=start + 0.0, end=start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=start + 0.0, end=start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=72, start=start + 0.0, end=start + 0.75))
    elif bar == 3:
        # G7 (G B D F)
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=start + 0.0, end=start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=start + 0.0, end=start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=start + 0.0, end=start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=start + 0.0, end=start + 0.75))
    elif bar == 4:
        # Cmaj7 (C E G B)
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=start + 0.0, end=start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=start + 0.0, end=start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=start + 0.0, end=start + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=start + 0.0, end=start + 0.75))

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []
bar = 2
start = bar * 1.5
# Motif: F#4 -> A4 -> D4 -> F#4 (chromatic approach on A)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=66, start=start + 0.0, end=start + 0.375))  # F#4
sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=start + 0.375, end=start + 0.75))  # A4
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=start + 0.75, end=start + 1.125))  # D4
sax_notes.append(pretty_midi.Note(velocity=100, pitch=66, start=start + 1.125, end=start + 1.5))  # F#4

# Repeat the motif with a slight variation
bar = 3
start = bar * 1.5
sax_notes.append(pretty_midi.Note(velocity=100, pitch=66, start=start + 0.0, end=start + 0.375))  # F#4
sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=start + 0.375, end=start + 0.75))  # A4
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=start + 0.75, end=start + 1.125))  # D4
sax_notes.append(pretty_midi.Note(velocity=100, pitch=66, start=start + 1.125, end=start + 1.5))  # F#4

# Final phrase, complete the motif
bar = 4
start = bar * 1.5
sax_notes.append(pretty_midi.Note(velocity=100, pitch=66, start=start + 0.0, end=start + 0.375))  # F#4
sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=start + 0.375, end=start + 0.75))  # A4
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=start + 0.75, end=start + 1.125))  # D4
sax_notes.append(pretty_midi.Note(velocity=100, pitch=66, start=start + 1.125, end=start + 1.5))  # F#4

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
