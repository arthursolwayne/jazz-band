
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.75),    # D2 (bar 2, beat 1)
    pretty_midi.Note(velocity=80, pitch=41, start=1.75, end=2.0),    # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.25),    # G2 (bar 2, beat 2)
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.5),    # E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=2.5, end=2.75),    # D2 (bar 2, beat 3)
    pretty_midi.Note(velocity=80, pitch=41, start=2.75, end=3.0),    # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.25),    # G2 (bar 3, beat 1)
    pretty_midi.Note(velocity=80, pitch=40, start=3.25, end=3.5),    # E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=3.5, end=3.75),    # D2 (bar 3, beat 2)
    pretty_midi.Note(velocity=80, pitch=41, start=3.75, end=4.0),    # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=4.0, end=4.25),    # G2 (bar 3, beat 3)
    pretty_midi.Note(velocity=80, pitch=40, start=4.25, end=4.5),    # E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.75),    # D2 (bar 4, beat 1)
    pretty_midi.Note(velocity=80, pitch=41, start=4.75, end=5.0),    # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=5.0, end=5.25),    # G2 (bar 4, beat 2)
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.5),    # E2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # C5
]
# Bar 3: Gm7 (G Bb D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=2.75),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=2.75),  # F5
])
# Bar 4: Cm7 (C Eb G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=3.5, end=3.75),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # Bb4
])
# Resolving chord on bar 4 (Dm7 again)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # C5
])
piano.notes.extend(piano_notes)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - G4 - D4 (quarter notes)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # D4
    # Repeat the motif with a slight variation, leaving it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.25),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.5),  # D4
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    # Bar start time
    start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hihat on 2
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on 4
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.875)

drums.notes.extend(drums.notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
