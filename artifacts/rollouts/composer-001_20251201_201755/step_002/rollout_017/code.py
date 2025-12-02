
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875)    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass - walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=80, pitch=55, start=1.875, end=2.25), # Ab (E2)
    pretty_midi.Note(velocity=80, pitch=54, start=2.25, end=2.625), # G (D#2)
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0),  # F (D2)
]
bass.notes.extend(bass_notes)

# Diane on piano - open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),  # E

    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625), # Ab

    # Bar 4: Dmin7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),  # C
]
piano.notes.extend(piano_notes)

# Little Ray on drums (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Dante on sax - one short motif, make it sing
# Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.6875), # A (start of motif)
    pretty_midi.Note(velocity=110, pitch=69, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.4375), # A (return)
    pretty_midi.Note(velocity=110, pitch=69, start=2.4375, end=2.625), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.8125), # B
    pretty_midi.Note(velocity=110, pitch=66, start=2.8125, end=3.0),  # A (finish)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
