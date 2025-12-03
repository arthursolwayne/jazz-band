
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in Fm (F, Ab, D, C, F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=3.0),  # C2
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75), # Ab2
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),  # C2
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25), # Ab2
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.625), # D2
    pretty_midi.Note(velocity=100, pitch=55, start=5.625, end=6.0)   # C2
]
bass.notes.extend(bass_notes)

# Diane - Open voicings, resolving on the last chord of each bar
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625), # F4
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.625), # Ab4
]
# Bar 4: Fm7 (F, Ab, C, D)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),  # Ab4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
]
piano.notes.extend(piano_notes)

# Dante - Tenor sax motif: F, Ab, C, Eb, G, Bb, Ab, F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # F5
    pretty_midi.Note(velocity=100, pitch=73, start=1.875, end=2.25), # Ab5
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # C5
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # Eb5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G5
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75), # Bb5
    pretty_midi.Note(velocity=100, pitch=73, start=3.75, end=4.125), # Ab5
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),  # F5
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [1.5, 3.0, 4.5]:
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar, end=bar + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar + 1.125, end=bar + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar + 0.75, end=bar + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=bar + 1.875, end=bar + 2.0)
    # Hi-hat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=100, pitch=42, start=bar + i * 0.1875, end=bar + i * 0.1875 + 0.1875)

drums.notes.extend([n for n in locals().values() if isinstance(n, pretty_midi.Note)])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
