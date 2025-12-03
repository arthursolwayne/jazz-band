
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick = pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375)
snare = pretty_midi.Note(velocity=80, pitch=38, start=0.75, end=1.125)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5)
hihat2 = pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.75)
hihat3 = pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.125)
hihat4 = pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5)

drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=70, pitch=41, start=1.875, end=2.25), # F2 (chromatic approach to G2)
    pretty_midi.Note(velocity=70, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=70, pitch=38, start=2.625, end=3.0),  # D2
]

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.75),  # C5
]

# Dante: Melodic motif - start it, leave it hanging, then finish it
# Dm scale: D, Eb, F, G, A, Bb, C, D
# Motif: D (1.5s), Eb (1.875s), F (2.25s), leave it hanging, return at 2.625s with D again
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.0),   # Eb4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.375), # F4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.75)  # D4 (resolution)
]

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes.extend([
    pretty_midi.Note(velocity=70, pitch=41, start=3.0, end=3.375),  # F2 (chromatic approach to G2)
    pretty_midi.Note(velocity=70, pitch=43, start=3.375, end=3.75),  # G2
    pretty_midi.Note(velocity=70, pitch=38, start=3.75, end=4.125),  # D2
    pretty_midi.Note(velocity=70, pitch=41, start=4.125, end=4.5),   # F2
])

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: D7 (D-F#-A-C)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.25),  # C5
])

# Dante: Melodic motif continuation
# Continue the motif, lead into resolution
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.125),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),   # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.875),  # D4 (resolution)
])

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes.extend([
    pretty_midi.Note(velocity=70, pitch=43, start=4.5, end=4.875),  # G2
    pretty_midi.Note(velocity=70, pitch=38, start=4.875, end=5.25),  # D2
    pretty_midi.Note(velocity=70, pitch=41, start=5.25, end=5.625),  # F2
    pretty_midi.Note(velocity=70, pitch=43, start=5.625, end=6.0),   # G2
])

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: Dm7 (D-F-A-C)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.75),  # C5
])

# Dante: Melodic resolution
# End the motif with D, close the idea
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0),   # D4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.375),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.75)  # D4
])

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 3.0s
kick = pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.875)
snare = pretty_midi.Note(velocity=80, pitch=38, start=2.25, end=2.625)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=1.5, end=3.0)
hihat2 = pretty_midi.Note(velocity=60, pitch=42, start=1.875, end=2.25)
hihat3 = pretty_midi.Note(velocity=60, pitch=42, start=2.25, end=2.625)
hihat4 = pretty_midi.Note(velocity=60, pitch=42, start=2.625, end=3.0)

drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Bar 3: 3.0 - 4.5s
kick = pretty_midi.Note(velocity=80, pitch=36, start=3.0, end=3.375)
snare = pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=3.0, end=4.5)
hihat2 = pretty_midi.Note(velocity=60, pitch=42, start=3.375, end=3.75)
hihat3 = pretty_midi.Note(velocity=60, pitch=42, start=3.75, end=4.125)
hihat4 = pretty_midi.Note(velocity=60, pitch=42, start=4.125, end=4.5)

drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Bar 4: 4.5 - 6.0s
kick = pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.875)
snare = pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.625)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=6.0)
hihat2 = pretty_midi.Note(velocity=60, pitch=42, start=4.875, end=5.25)
hihat3 = pretty_midi.Note(velocity=60, pitch=42, start=5.25, end=5.625)
hihat4 = pretty_midi.Note(velocity=60, pitch=42, start=5.625, end=6.0)

drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Add notes to instruments
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
