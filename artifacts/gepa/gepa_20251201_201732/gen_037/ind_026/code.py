
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
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),    # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),    # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),    # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),    # E
    # Bar 3: C7
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),    # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),    # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),    # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),    # Bb
    # Bar 4: Am7
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),    # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),    # C
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),    # E
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),    # G
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F, G, Ab, F (motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # F
    # Repeat the motif
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 1.5)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.5)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    # Add to drums
    drums.notes.extend([kick, snare, kick2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])
