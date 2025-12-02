
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375), # kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375), # hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75), # hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125), # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5), # kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5), # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875), # hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass (Marcus): Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=37, start=1.5, end=1.875), # F (root)
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.25), # Ab (fifth)
    pretty_midi.Note(velocity=90, pitch=38, start=2.25, end=2.625), # Gb (chromatic)
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0), # Bb (root)
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, resolving on the last chord
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=53, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=95, pitch=50, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=95, pitch=48, start=1.5, end=1.875), # Ab
    pretty_midi.Note(velocity=95, pitch=55, start=1.5, end=1.875), # F
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=58, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=95, pitch=55, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=95, pitch=53, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=95, pitch=50, start=2.25, end=2.625), # Bb
])
# Bar 4: Eb7 (Eb, G, Bb, Db)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=62, start=2.625, end=3.0), # Db
    pretty_midi.Note(velocity=95, pitch=58, start=2.625, end=3.0), # Bb
    pretty_midi.Note(velocity=95, pitch=55, start=2.625, end=3.0), # G
    pretty_midi.Note(velocity=95, pitch=53, start=2.625, end=3.0), # Eb
])
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing
# Start with a phrase that leans into the tension and resolves with a question
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=1.5, end=1.75), # G (Fm7)
    pretty_midi.Note(velocity=105, pitch=65, start=1.75, end=2.0), # Bb (Bb7)
    pretty_midi.Note(velocity=105, pitch=61, start=2.0, end=2.25), # Ab (Eb7)
    pretty_midi.Note(velocity=105, pitch=63, start=2.25, end=2.5), # B (rest)
    pretty_midi.Note(velocity=105, pitch=62, start=2.5, end=2.75), # G (rest)
    pretty_midi.Note(velocity=105, pitch=60, start=2.75, end=3.0), # F (rest)
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Same pattern, but slightly more intensity
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375), # hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75), # hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125), # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5), # kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5), # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875), # snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875), # hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Drums (4.5 - 6.0s)
# Same pattern, but with a slight fill before the end
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875), # hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25), # hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625), # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0), # kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0), # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375), # snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375), # hihat on 4
]
drums.notes.extend(drum_notes)

# Add fills and variations in bar 3 and 4
# Bar 3 fill
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.0), # hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.0), # snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.0, end=4.375), # hihat on 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.0, end=4.375), # kick on 3
]
drums.notes.extend(drum_notes)

# Bar 4 fill
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.125), # hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.125), # snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.125, end=5.5), # hihat on 3
    pretty_midi.Note(velocity=100, pitch=36, start=5.125, end=5.5), # kick on 3
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("fm_intro.mid")
