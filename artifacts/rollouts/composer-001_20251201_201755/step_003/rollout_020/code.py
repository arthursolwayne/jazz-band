
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

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
# Bar 2: Fm (F, C)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25), # E (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625), # C (fifth)
    pretty_midi.Note(velocity=100, pitch=75, start=2.625, end=3.0),  # B (chromatic approach)
]
# Bar 3: Bb7 (Bb, F)
bass_notes += [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Bb (root)
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75), # A (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125), # F (fifth)
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),  # E (chromatic approach)
]
# Bar 4: Eb7 (Eb, Bb)
bass_notes += [
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875),  # Eb (root)
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # D (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625), # Bb (fifth)
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # A (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),  # D
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # Ab
]
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.75),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (71) - G (72) - F (71) - E (70)
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=70, start=2.625, end=3.0),   # E
]
# Bar 3: Leave it hanging (no sax)
# Bar 4: Come back and finish it, but change the ending to E (70) - D (69) - C (67) - Bb (67)
sax_notes += [
    pretty_midi.Note(velocity=110, pitch=70, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0),   # Bb
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 4
]
# Bar 3
drum_notes += [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 4
]
# Bar 4
drum_notes += [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
