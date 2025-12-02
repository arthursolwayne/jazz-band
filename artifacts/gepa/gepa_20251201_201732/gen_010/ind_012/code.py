
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

# Bass: Walking line in Fm (F, Ab, D, C)
# Bar 2: F (root), Ab (b9), D (5), C (b7)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # Ab2 (b9)
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625), # D3 (5)
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=3.0),  # C3 (b7)
    
    # Bar 3: Ab (b9), F (root), C (b7), Bb (b6)
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # Ab2
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.125), # C3
    pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.5),  # Bb2
    
    # Bar 4: D (5), C (b7), F (root), Ab (b9)
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),  # D3
    pretty_midi.Note(velocity=80, pitch=48, start=4.875, end=5.25), # C3
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625), # F2
    pretty_midi.Note(velocity=80, pitch=40, start=5.625, end=6.0),  # Ab2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.875),  # Ab2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # C3
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D3
    
    # Bar 3: Ab7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),  # Ab2
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),  # C3
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),  # Eb2
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # G3
    
    # Bar 4: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.875),  # Ab2
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # D3
]
piano.notes.extend(piano_notes)

# Sax: Motif — one short phrase, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: E (Ab), G (Bb), F (C), D (Bb) — imply Fm but with tension
# Bar 2: Start motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=41, start=1.5, end=1.875),  # E (Ab)
    pretty_midi.Note(velocity=100, pitch=44, start=1.875, end=2.25), # G (Bb)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # F (C)
    pretty_midi.Note(velocity=100, pitch=49, start=2.625, end=3.0),  # D (Bb)
    
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # F (C)
    
    # Bar 4: Return and finish it
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875),  # G (Bb)
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25), # E (Ab)
    pretty_midi.Note(velocity=100, pitch=49, start=5.25, end=5.625), # D (Bb)
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),  # F (C)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.875)

drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
