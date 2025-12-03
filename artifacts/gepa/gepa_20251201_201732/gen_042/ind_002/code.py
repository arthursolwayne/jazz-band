
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass (walking line in F, roots and fifths with chromatic approaches)
bass_notes = [
    # Bar 2: F - G - A - Bb
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625), # A2
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0), # Ab2 (chromatic approach)
    # Bar 3: Bb - C - D - Eb
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375), # Bb2
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75), # C2
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=90, pitch=73, start=4.125, end=4.5), # Db2 (chromatic approach)
    # Bar 4: Eb - F - G - A
    pretty_midi.Note(velocity=90, pitch=73, start=4.5, end=4.875), # Eb2
    pretty_midi.Note(velocity=90, pitch=70, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0), # A2
]
bass.notes.extend(bass_notes)

# Diane on piano (open voicings, different chord each bar, resolve on the last)
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # A2
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # C2 (repeat for presence)
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875), # E2
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # Bb2
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375), # D2
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375), # F2
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # Ab2
    # Bar 4: Ebmaj7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.875), # Eb2
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875), # G2
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # Bb2
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875), # D2
]
piano.notes.extend(piano_notes)

# Dante on sax (motif that sings, one phrase, leave it hanging)
sax_notes = [
    # Bar 2: Phrase starts
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.75), # A4 (F in F)
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0), # G4 (Bb)
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25), # A4 (C)
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5), # G4 (D)
    # Bar 3: Same motif delayed
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25), # A4
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5), # G4
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75), # A4
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0), # G4
    # Bar 4: Return to the motif, finish it
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75), # A4
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0), # G4
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.25), # A4
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5), # G4
    pretty_midi.Note(velocity=110, pitch=69, start=5.5, end=5.75), # A4
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0), # G4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
