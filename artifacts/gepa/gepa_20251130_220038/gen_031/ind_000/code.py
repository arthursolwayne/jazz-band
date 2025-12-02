
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
hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375)
hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75)
hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125)
hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)

drums.notes.extend([kick1, snare1, hihat1, hihat2, hihat3, hihat4, kick2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
# D Dorian: D E F# G A B C
# Start on D, walk in half steps: D Eb F G Ab Bb B

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0), # G
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375), # Ab
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5), # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875), # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0), # Ab
]

bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
# D7: D F# A C
# Dm7: D F A C
# D7 on beat 2, Dm7 on beat 4

diane_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875), # C
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.625), # C
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375), # C
    # Repeat same chords in bar 4 for comping
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0), # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0), # A
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0), # C
]

piano.notes.extend(diane_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 2
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
hihat5 = pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875)
hihat6 = pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25)
hihat7 = pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625)
hihat8 = pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)

# Bar 3
kick5 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
hihat9 = pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375)
hihat10 = pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75)
hihat11 = pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125)
hihat12 = pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5)
kick6 = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)

# Bar 4
kick7 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare4 = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
hihat13 = pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875)
hihat14 = pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25)
hihat15 = pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625)
hihat16 = pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
kick8 = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)

drums.notes.extend([kick3, snare2, hihat5, hihat6, hihat7, hihat8, kick4,
                    kick5, snare3, hihat9, hihat10, hihat11, hihat12, kick6,
                    kick7, snare4, hihat13, hihat14, hihat15, hihat16, kick8])

# Dante: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# D Dorian: D E F# G A B C
# Motif: D F# G A (whisper), then A B D (cry)

# Bar 2
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875), # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0625), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.0625, end=2.25), # A

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.625), # B
    pretty_midi.Note(velocity=100, pitch=62, start=3.625, end=3.875), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.375), # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.375, end=4.5), # B
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75), # D

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0), # G
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_moment.mid")
