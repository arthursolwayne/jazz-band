
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (Fm) - D2-G2, roots and fifths with chromatic approaches
# Bar 2: Fm (F, C, D, Bb)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25), # C3
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625), # D3
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # Bb2
    # Bar 3: Abm7 (Ab, Eb, F, C)
    pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.375),  # Ab2
    pretty_midi.Note(velocity=90, pitch=73, start=3.375, end=3.75), # Eb3
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125), # F3
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.5),  # C3
    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # D3
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.25), # F#3
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625), # A3
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0),  # C3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.875),  # F3
    pretty_midi.Note(velocity=95, pitch=68, start=1.5, end=1.875),  # Ab3
    pretty_midi.Note(velocity=95, pitch=76, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=95, pitch=72, start=1.5, end=1.875),  # D4
    # Bar 3: Abm7 (Ab, C, Eb, F)
    pretty_midi.Note(velocity=95, pitch=68, start=3.0, end=3.375),  # Ab3
    pretty_midi.Note(velocity=95, pitch=76, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=95, pitch=73, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.375),  # F4
    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=95, pitch=72, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=95, pitch=77, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=95, pitch=74, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=95, pitch=76, start=4.5, end=4.875),  # C5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - D - F (a short melodic line)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F3
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),   # Bb3
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # F3
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # F3
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # Bb3
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # F3
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # F3
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # Bb3
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # F3
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75),  # F3
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # Bb3
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2 (1.5 - 3.0)
for i in range(4):
    pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i * 0.75, end=1.5 + i * 0.75 + 0.375)  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.5 + i * 0.75 + 0.375, end=1.5 + i * 0.75 + 0.5)  # Snare
    for j in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=1.5 + i * 0.75 + j * 0.375, end=1.5 + i * 0.75 + j * 0.375 + 0.375)  # Hi-hat

# Bar 3 (3.0 - 4.5)
for i in range(4):
    pretty_midi.Note(velocity=100, pitch=36, start=3.0 + i * 0.75, end=3.0 + i * 0.75 + 0.375)  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.0 + i * 0.75 + 0.375, end=3.0 + i * 0.75 + 0.5)  # Snare
    for j in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=3.0 + i * 0.75 + j * 0.375, end=3.0 + i * 0.75 + j * 0.375 + 0.375)  # Hi-hat

# Bar 4 (4.5 - 6.0)
for i in range(4):
    pretty_midi.Note(velocity=100, pitch=36, start=4.5 + i * 0.75, end=4.5 + i * 0.75 + 0.375)  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.5 + i * 0.75 + 0.375, end=4.5 + i * 0.75 + 0.5)  # Snare
    for j in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=4.5 + i * 0.75 + j * 0.375, end=4.5 + i * 0.75 + j * 0.375 + 0.375)  # Hi-hat

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
