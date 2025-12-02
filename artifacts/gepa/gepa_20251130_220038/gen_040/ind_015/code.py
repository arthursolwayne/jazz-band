
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=42, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=44, start=2.0, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=43, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=44, start=3.25, end=3.5),  # F#
    pretty_midi.Note(velocity=90, pitch=45, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=40, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=90, pitch=41, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=90, pitch=45, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=42, start=5.5, end=5.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=44, start=5.75, end=6.0),  # F#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4.
# Fm7 = F Ab C Eb
# Bb7 = Bb D F Ab
# Fm7 = F Ab C Eb
# Bb7 = Bb D F Ab

piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),  # Eb
    
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5),  # Ab
    
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0),  # Eb
    
    # Bar 5
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.75),  # Ab
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C
# Motif: F - Bb - Ab - F# (chromatic approach to G)
# Repeat but end on Bb

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75), # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=1.875), # Ab
    pretty_midi.Note(velocity=110, pitch=70, start=1.875, end=2.0),  # F# (approach to G)
    
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.375, end=2.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=2.5, end=2.625),  # Ab
    pretty_midi.Note(velocity=110, pitch=70, start=2.625, end=2.75), # F# (approach to G)
    
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.25), # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.375), # Ab
    pretty_midi.Note(velocity=110, pitch=70, start=3.375, end=3.5),  # F# (approach to G)
    
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.875, end=4.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=4.0, end=4.125),  # Ab
    pretty_midi.Note(velocity=110, pitch=70, start=4.125, end=4.25), # F# (approach to G)
    
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.625, end=4.75), # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=4.875), # Ab
    pretty_midi.Note(velocity=110, pitch=70, start=4.875, end=5.0),  # F# (approach to G)
    
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5),  # Bb (finish the motif)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
