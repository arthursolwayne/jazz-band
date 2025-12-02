
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: D4 (D), F#4 (F#), A4 (A), G4 (G)
# D, F#, A, G - a simple motif with space
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.8125)
]
sax.notes.extend(sax_notes)

# Bass: walking line, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.6875), # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.6875, end=1.875), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.0625), # G2
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=2.25, end=2.4375), # D2
    pretty_midi.Note(velocity=80, pitch=40, start=2.4375, end=2.625), # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=2.8125), # G2
]
bass.notes.extend(bass_notes)

# Piano: open voicing, Dmaj7 (D, F#, A, C#), then G7 (G, B, D, F), then Am7 (A, C, E, G), then D7 (D, F#, A, C#)
# Comp on beat 2 and 4
piano_notes = [
    # Dmaj7 on beat 1
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.6875), # D4
    pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=1.6875), # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.6875), # A4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.6875), # C#4
    # G7 on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0625), # G4
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.0625), # B4
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0625), # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0625), # F4
    # Am7 on beat 3
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.4375), # A4
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.4375), # C4
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.4375), # E4
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.4375), # G4
    # D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=2.8125), # D4
    pretty_midi.Note(velocity=90, pitch=66, start=2.625, end=2.8125), # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.8125), # A4
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.8125), # C#4
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax repeats motif, but with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.4375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.625, end=3.8125),
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.1875)
]
sax.notes.extend(sax_notes)

# Bass: walking line, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.1875), # D2
    pretty_midi.Note(velocity=80, pitch=40, start=3.1875, end=3.375), # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.5625), # G2
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75), # F#2
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=3.9375), # D2
    pretty_midi.Note(velocity=80, pitch=40, start=3.9375, end=4.125), # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.3125), # G2
]
bass.notes.extend(bass_notes)

# Piano: open voicing, Dmaj7 (D, F#, A, C#), then G7 (G, B, D, F), then Am7 (A, C, E, G), then D7 (D, F#, A, C#)
# Comp on beat 2 and 4
piano_notes = [
    # Dmaj7 on beat 1
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.1875), # D4
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.1875), # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.1875), # A4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.1875), # C#4
    # G7 on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5625), # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.5625), # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5625), # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5625), # F4
    # Am7 on beat 3
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.9375), # A4
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=3.9375), # C4
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=3.9375), # E4
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.9375), # G4
    # D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.3125), # D4
    pretty_midi.Note(velocity=90, pitch=66, start=4.125, end=4.3125), # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.3125), # A4
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.3125), # C#4
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax finishes the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=5.8125)
]
sax.notes.extend(sax_notes)

# Bass: walking line, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.6875), # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.6875, end=4.875), # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.0625), # G2
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25), # F#2
    pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.4375), # D2
    pretty_midi.Note(velocity=80, pitch=40, start=5.4375, end=5.625), # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=5.625, end=5.8125), # G2
]
bass.notes.extend(bass_notes)

# Piano: open voicing, Dmaj7 (D, F#, A, C#), then G7 (G, B, D, F), then Am7 (A, C, E, G), then D7 (D, F#, A, C#)
# Comp on beat 2 and 4
piano_notes = [
    # Dmaj7 on beat 1
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.6875), # D4
    pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=4.6875), # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.6875), # A4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.6875), # C#4
    # G7 on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0625), # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.0625), # B4
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.0625), # D4
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0625), # F4
    # Am7 on beat 3
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.4375), # A4
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.4375), # C4
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.4375), # E4
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.4375), # G4
    # D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=5.8125), # D4
    pretty_midi.Note(velocity=90, pitch=66, start=5.625, end=5.8125), # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=5.8125), # A4
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=5.8125), # C#4
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.8125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=110, pitch=38, start=5.8125, end=6.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
