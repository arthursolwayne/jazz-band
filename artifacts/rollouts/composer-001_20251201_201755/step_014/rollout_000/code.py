
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25), # Eb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.625), # A (fifth)
    pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=3.0),  # Bb (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.875), # F (C4)
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875), # A (E4)
    pretty_midi.Note(velocity=85, pitch=79, start=1.5, end=1.875), # C (G4)
    pretty_midi.Note(velocity=80, pitch=74, start=1.5, end=1.875), # Eb (F4)
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=65, start=2.25, end=2.625), # Bb (D4)
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625), # D (F4)
    pretty_midi.Note(velocity=85, pitch=71, start=2.25, end=2.625), # F (G4)
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625), # Ab (E4)
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=79, start=3.0, end=3.375), # C (G4)
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375), # Eb (F4)
    pretty_midi.Note(velocity=85, pitch=82, start=3.0, end=3.375), # G (A4)
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375), # Bb (F4)
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (C4), Ab (E4), Bb (F4), Eb (D4)
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=71, start=1.5, end=1.875), # F (C4)
    pretty_midi.Note(velocity=105, pitch=67, start=1.875, end=2.25), # Ab (E4)
    pretty_midi.Note(velocity=105, pitch=69, start=2.25, end=2.625), # Bb (F4)
    pretty_midi.Note(velocity=105, pitch=74, start=2.625, end=3.0),  # Eb (D4)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # Bb (root)
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75), # A (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125), # D (fifth)
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),  # Eb (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=65, start=3.0, end=3.375), # Bb (D4)
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375), # D (F4)
    pretty_midi.Note(velocity=85, pitch=71, start=3.0, end=3.375), # F (G4)
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375), # Ab (E4)
]
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=79, start=3.75, end=4.125), # C (G4)
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125), # Eb (F4)
    pretty_midi.Note(velocity=85, pitch=82, start=3.75, end=4.125), # G (A4)
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125), # Bb (F4)
])
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=3.125, end=3.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    pretty_midi.Note(velocity=110, pitch=38, start=4.625, end=4.75),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.875),  # C (root)
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.25), # B (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=82, start=5.25, end=5.625), # E (fifth)
    pretty_midi.Note(velocity=90, pitch=83, start=5.625, end=6.0),  # F (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=79, start=4.5, end=4.875), # C (G4)
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875), # Eb (F4)
    pretty_midi.Note(velocity=85, pitch=82, start=4.5, end=4.875), # G (A4)
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875), # Bb (F4)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (C4), Ab (E4), Bb (F4), Eb (D4)
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=71, start=4.5, end=4.875), # F (C4)
    pretty_midi.Note(velocity=105, pitch=67, start=4.875, end=5.25), # Ab (E4)
    pretty_midi.Note(velocity=105, pitch=69, start=5.25, end=5.625), # Bb (F4)
    pretty_midi.Note(velocity=105, pitch=74, start=5.625, end=6.0),  # Eb (D4)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
