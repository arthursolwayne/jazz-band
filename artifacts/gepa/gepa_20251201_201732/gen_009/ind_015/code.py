
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm (F2, Ab2, D2, G2, etc.)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.25), # Eb2 (flat 7)
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625), # D2 (flat 3)
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),  # G2 (5th)
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # F2 (root)
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75), # Eb2 (flat 7)
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125), # D2 (flat 3)
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),  # G2 (5th)
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F2 (root)
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.25), # Eb2 (flat 7)
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625), # D2 (flat 3)
    pretty_midi.Note(velocity=90, pitch=55, start=5.625, end=6.0),  # G2 (5th)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chords each bar
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # D5
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # F5
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Ab4
])
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # D5
])
piano.notes.extend(piano_notes)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    # Snare on 3
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2, starting on beat 2
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # G4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # G4
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # F4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
