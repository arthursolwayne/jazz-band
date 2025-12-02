
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
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drum_hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
drum_hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125)
drum_hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat, drum_hihat2, drum_hihat3, drum_hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
# Starting on D (2nd fret of E string), walking in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.625), # C#
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5), # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25), # C#
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0), # Eb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
# Dm7: D, F, A, C
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # G

    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375), # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # G

    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # G
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 3.0s
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
drum_hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0)
drum_hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25)
drum_hihat7 = pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625)
drum_hihat8 = pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
drums.notes.extend([drum_kick2, drum_snare2, drum_hihat5, drum_hihat6, drum_hihat7, drum_hihat8])

# Bar 3: 3.0 - 4.5s
drum_kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_snare3 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
drum_hihat9 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.5)
drum_hihat10 = pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75)
drum_hihat11 = pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125)
drum_hihat12 = pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5)
drums.notes.extend([drum_kick3, drum_snare3, drum_hihat9, drum_hihat10, drum_hihat11, drum_hihat12])

# Bar 4: 4.5 - 6.0s
drum_kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_snare4 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
drum_hihat13 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.0)
drum_hihat14 = pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25)
drum_hihat15 = pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625)
drum_hihat16 = pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)
drums.notes.extend([drum_kick4, drum_snare4, drum_hihat13, drum_hihat14, drum_hihat15, drum_hihat16])

# Dante: Tenor sax - one short motif, make it sing
# Dm7: D, F, A, C
# Start on D, then F, then A, then C suspended for a half beat
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0), # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # G (sustained)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5), # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # G (sustained)
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0), # Eb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
