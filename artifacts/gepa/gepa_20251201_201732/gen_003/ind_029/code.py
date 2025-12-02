
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line (F2, G2, A2, Bb2, C3, D3, Eb3, F3), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=55, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=80, pitch=57, start=2.25, end=2.625), # A2
    pretty_midi.Note(velocity=80, pitch=58, start=2.625, end=3.0),  # Bb2
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),  # C3
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75), # D3
    pretty_midi.Note(velocity=80, pitch=63, start=3.75, end=4.125), # Eb3
    pretty_midi.Note(velocity=80, pitch=53, start=4.125, end=4.5),  # F2
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.875),  # G2
    pretty_midi.Note(velocity=80, pitch=52, start=4.875, end=5.25), # F2 chromatic approach
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.625), # F2
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0)   # C3
]
bass.notes.extend(bass_notes)

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    # Bar 2: F7
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=90, pitch=78, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=90, pitch=82, start=1.5, end=1.875), # E

    # Bar 3: Bb7
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=90, pitch=77, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=78, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=80, start=2.25, end=2.625), # Ab

    # Bar 4: Cm7
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375), # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375), # Bb
]
piano.notes.extend(piano_notes)

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0),    # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.25),  # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=2.875, end=3.0),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),   # Hihat

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0), # Hihat
]
drums.notes.extend(drum_notes)

# Dante on sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Bb, C, F (half note, quarter note, eighth note, eighth note)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0), # F (half note)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=78, start=3.375, end=3.5), # C
    pretty_midi.Note(velocity=100, pitch=78, start=3.5, end=3.625), # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.625, end=3.75) # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
