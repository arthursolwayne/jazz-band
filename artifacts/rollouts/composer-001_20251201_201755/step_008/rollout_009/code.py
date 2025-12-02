
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
    # Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)
# Bass: Walking line (D2-G2), roots and fifths with chromatic approaches

# Bar 2 (1.5 - 3.0s)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),   # D2 (root)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0),   # E2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Bar 3 (3.0 - 4.5s)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),   # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),   # E2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Bar 4 (4.5 - 6.0s)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),   # D2 (root)
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),   # E2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2 (1.5 - 3.0s): D7 (open voicing)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),   # D4 (root)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),   # G4 (fifth)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),   # C5 (seventh)
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0),   # D5 (ninth)
]
piano.notes.extend(piano_notes)

# Bar 3 (3.0 - 4.5s): Bm7 (open voicing)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),   # B4 (root)
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),   # D5 (fifth)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),   # A4 (seventh)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),   # F#5 (ninth)
]
piano.notes.extend(piano_notes)

# Bar 4 (4.5 - 6.0s): Gmaj7 (open voicing)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),   # G4 (root)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),   # C5 (fifth)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),   # F#5 (seventh)
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0),   # B5 (ninth)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - G4 - E4 (with a slight delay on E4 to leave it hanging)

# Bar 2: Start motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25), # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625), # G4
]
sax.notes.extend(sax_notes)

# Bar 3: Let it hang
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=4.5),    # F#4 (sustained)
]
sax.notes.extend(sax_notes)

# Bar 4: Complete the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=5.25),   # E4 (resolve on 1)
]
sax.notes.extend(sax_notes)

# Drums in bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hi-hats
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75)
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
