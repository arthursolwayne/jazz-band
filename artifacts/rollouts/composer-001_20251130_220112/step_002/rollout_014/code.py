
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

kick1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375)
hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75)
hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125)
hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)

kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)

drums.notes.extend([kick1, snare1, hihat1, hihat2, hihat3, hihat4, kick2, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),  # D
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875),  # D7
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=74, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=77, start=1.5, end=1.875),

    # Bar 3
    pretty_midi.Note(velocity=80, pitch=70, start=2.625, end=2.875),
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=2.875),
    pretty_midi.Note(velocity=80, pitch=74, start=2.625, end=2.875),
    pretty_midi.Note(velocity=80, pitch=77, start=2.625, end=2.875),

    # Bar 4
    pretty_midi.Note(velocity=80, pitch=70, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=77, start=3.75, end=4.0),
]

piano.notes.extend(piano_notes)

# Sax: Your motif, short and singable
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),   # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # E
]

sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 2
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
hihat5 = pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875)
hihat6 = pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25)
hihat7 = pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625)
hihat8 = pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)

# Bar 3
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875)
snare4 = pretty_midi.Note(velocity=100, pitch=38, start=2.875, end=3.25)
hihat9 = pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.875)
hihat10 = pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.25)
hihat11 = pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.625)
hihat12 = pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=4.0)

# Bar 4
kick5 = pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)
snare5 = pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5)
hihat13 = pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125)
hihat14 = pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5)
hihat15 = pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875)
hihat16 = pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25)

# Final kick and snare
kick6 = pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625)
snare6 = pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0)
hihat17 = pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625)
hihat18 = pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)

drums.notes.extend([kick3, snare3, hihat5, hihat6, hihat7, hihat8,
                   kick4, snare4, hihat9, hihat10, hihat11, hihat12,
                   kick5, snare5, hihat13, hihat14, hihat15, hihat16,
                   kick6, snare6, hihat17, hihat18])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
