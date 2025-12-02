
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (D2-G2, MIDI 38-43), walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),   # D2 on 2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # Eb2 on 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2 on 4
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),   # D2 on 1
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),   # Eb2 on 2
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75),  # G2 on 3
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),  # F2 on 4
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),   # D2 on 1
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.875),   # Eb2 on 2
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25),  # G2 on 3
    pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.625),  # F2 on 4
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0)    # D2 on 1
]
bass.notes.extend(bass_notes)

# Piano: Diane (open voicings, resolve on the last beat of each bar)
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=1.875),  # D
]
# Bar 3: Bbmaj7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625),  # Ab
])
# Bar 4: Fm7 (F, Ab, C, D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.375),  # D
])
# Bar 2: comp on 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=73, start=1.875, end=2.25),  # D
])
# Bar 3: comp on 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),  # Ab
])
# Bar 4: comp on 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.875),  # D
])
piano.notes.extend(piano_notes)

# Sax: Dante (one short motif, make it sing)
# Bar 2: Start motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # Eb (melody starts)
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # D
    # Bar 3: Return to motif
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # D
    # Bar 4: Finish motif, leave it hanging
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # D
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
