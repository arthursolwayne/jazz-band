
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus - walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.625, end=1.75), # F#
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=1.875), # G
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.0), # G#
    pretty_midi.Note(velocity=90, pitch=52, start=2.0, end=2.125), # A
    pretty_midi.Note(velocity=90, pitch=53, start=2.125, end=2.25), # A#
    pretty_midi.Note(velocity=90, pitch=54, start=2.25, end=2.375), # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=2.375, end=2.5), # B
    pretty_midi.Note(velocity=90, pitch=56, start=2.5, end=2.625), # C
    pretty_midi.Note(velocity=90, pitch=57, start=2.625, end=2.75), # C#
    pretty_midi.Note(velocity=90, pitch=58, start=2.75, end=2.875), # D
    pretty_midi.Note(velocity=90, pitch=59, start=2.875, end=3.0), # D#
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.125), # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=3.125, end=3.25), # E
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.375), # F
    pretty_midi.Note(velocity=90, pitch=63, start=3.375, end=3.5), # F#
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.625), # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.625, end=3.75), # G#
    pretty_midi.Note(velocity=90, pitch=66, start=3.75, end=3.875), # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.875, end=4.0), # A#
    pretty_midi.Note(velocity=90, pitch=68, start=4.0, end=4.125), # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.25), # B
    pretty_midi.Note(velocity=90, pitch=70, start=4.25, end=4.375), # C
    pretty_midi.Note(velocity=90, pitch=71, start=4.375, end=4.5), # C#
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.625), # D
    pretty_midi.Note(velocity=90, pitch=73, start=4.625, end=4.75), # D#
    pretty_midi.Note(velocity=90, pitch=74, start=4.75, end=4.875), # Eb
    pretty_midi.Note(velocity=90, pitch=75, start=4.875, end=5.0), # E
    pretty_midi.Note(velocity=90, pitch=76, start=5.0, end=5.125), # F
    pretty_midi.Note(velocity=90, pitch=77, start=5.125, end=5.25), # F#
    pretty_midi.Note(velocity=90, pitch=78, start=5.25, end=5.375), # G
    pretty_midi.Note(velocity=90, pitch=79, start=5.375, end=5.5), # G#
    pretty_midi.Note(velocity=90, pitch=80, start=5.5, end=5.625), # A
    pretty_midi.Note(velocity=90, pitch=81, start=5.625, end=5.75), # A#
    pretty_midi.Note(velocity=90, pitch=82, start=5.75, end=5.875), # Bb
    pretty_midi.Note(velocity=90, pitch=83, start=5.875, end=6.0), # B
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.625), # C
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.625), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625), # G

    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.375), # B
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.375), # C
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.375), # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.375), # F

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.125), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125), # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.125), # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125), # A

    pretty_midi.Note(velocity=100, pitch=59, start=3.75, end=3.875), # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.875), # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.875), # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.875), # A

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.625), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625), # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625), # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.625), # A

    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.375), # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.375), # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.375), # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.375), # C#
]
piano.notes.extend(piano_notes)

# Sax: Dante - motif with space and tension
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.0), # G
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.375), # A
    pretty_midi.Note(velocity=110, pitch=61, start=2.625, end=2.75), # E

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125), # F
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.5), # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=3.875), # B
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.25), # A

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625), # F
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.0), # G
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.375), # A
    pretty_midi.Note(velocity=110, pitch=61, start=5.625, end=5.75), # E
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
