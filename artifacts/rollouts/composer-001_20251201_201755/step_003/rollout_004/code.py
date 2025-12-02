
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, roots and fifths with chromatic approaches, in Fm
# Fm: F, Ab, D, C, Bb, Eb, A, G
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25), # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # C2
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75), # D2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125), # Bb2
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),  # B2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=46, start=4.5, end=4.875),  # E2
    pretty_midi.Note(velocity=90, pitch=47, start=4.875, end=5.25), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=48, start=5.25, end=5.625), # F2
    pretty_midi.Note(velocity=90, pitch=49, start=5.625, end=6.0),  # G2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # Ab3
    pretty_midi.Note(velocity=100, pitch=56, start=1.5, end=1.875),  # C3
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # Eb3
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # Bb2
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625),  # D3
    pretty_midi.Note(velocity=100, pitch=56, start=2.25, end=2.625),  # F3
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # Ab3
])
# Bar 4: Fm7 (F, Ab, C, Eb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # Ab3
    pretty_midi.Note(velocity=100, pitch=56, start=3.0, end=3.375),  # C3
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # Eb3
])
# Bar 4 (continued): Dm7 (D, F, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),  # D2
    pretty_midi.Note(velocity=100, pitch=56, start=3.375, end=3.75),  # F3
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # A3
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # C3
])
# Bar 4 (continued): G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125),  # G2
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # B3
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # D4
    pretty_midi.Note(velocity=100, pitch=56, start=3.75, end=4.125),  # F3
])
# Bar 4 (continued): Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5),  # C2
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # Eb3
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # G3
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),  # Bb2
])
# Bar 4 (continued): Fm7 (F, Ab, C, Eb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # Ab3
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # Eb3
])
# Bar 4 (continued): Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25),  # Bb2
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25),  # D3
    pretty_midi.Note(velocity=100, pitch=56, start=4.875, end=5.25),  # F3
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # Ab3
])
# Bar 4 (continued): Fm7 (F, Ab, C, Eb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=48, start=5.25, end=5.625),  # F2
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625),  # Ab3
    pretty_midi.Note(velocity=100, pitch=56, start=5.25, end=5.625),  # C3
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # Eb3
])
# Bar 4 (continued): Dm7 (D, F, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),  # D2
    pretty_midi.Note(velocity=100, pitch=56, start=5.625, end=6.0),  # F3
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # A3
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # C3
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, C (Fm scale, but with a twist)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.6875),  # F2
    pretty_midi.Note(velocity=100, pitch=53, start=1.6875, end=1.875), # Ab2
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.0625), # Bb2
    pretty_midi.Note(velocity=100, pitch=52, start=2.0625, end=2.25), # C2
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.4375), # Bb2
    pretty_midi.Note(velocity=100, pitch=53, start=2.4375, end=2.625), # Ab2
    pretty_midi.Note(velocity=100, pitch=48, start=2.625, end=2.8125), # F2
    pretty_midi.Note(velocity=100, pitch=52, start=2.8125, end=3.0),  # C2
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.1875),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=3.1875, end=3.375), # Ab2
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.5625), # Bb2
    pretty_midi.Note(velocity=100, pitch=52, start=3.5625, end=3.75), # C2
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=3.9375), # Bb2
    pretty_midi.Note(velocity=100, pitch=53, start=3.9375, end=4.125), # Ab2
    pretty_midi.Note(velocity=100, pitch=48, start=4.125, end=4.3125), # F2
    pretty_midi.Note(velocity=100, pitch=52, start=4.3125, end=4.5),  # C2
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.6875),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=4.6875, end=4.875), # Ab2
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.0625), # Bb2
    pretty_midi.Note(velocity=100, pitch=52, start=5.0625, end=5.25), # C2
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.4375), # Bb2
    pretty_midi.Note(velocity=100, pitch=53, start=5.4375, end=5.625), # Ab2
    pretty_midi.Note(velocity=100, pitch=48, start=5.625, end=5.8125), # F2
    pretty_midi.Note(velocity=100, pitch=52, start=5.8125, end=6.0),  # C2
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
