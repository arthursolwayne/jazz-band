
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

# Kick on 1 and 3
drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick_2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.extend([drum_kick_1, drum_kick_2])

# Snare on 2 and 4
drum_snare_1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drums.notes.extend([drum_snare_1, drum_snare_2])

# Hi-hats on every eighth
hihat_notes = []
for i in range(0, 6):
    start = i * 0.375
    end = start + 0.375
    hihat_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))
drums.notes.extend(hihat_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line (Marcus) - walking line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # A
]
bass.notes.extend(bass_notes)

# Piano (Diane) - comping on 2 and 4
# Bar 2: D7 chord (F#9) on beat 2
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=95, pitch=71, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=95, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=95, pitch=76, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=95, pitch=79, start=1.875, end=2.25),  # F#
]
piano.notes.extend(piano_notes)

# Sax (Dante) - motif: D, F#, A (Dorian)
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=105, pitch=66, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=105, pitch=69, start=2.25, end=2.625), # A
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line (Marcus) - walking line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),   # D
]
bass.notes.extend(bass_notes)

# Piano (Diane) - comping on 2 and 4
# Bar 3: D7 chord (F#9) on beat 2
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=95, pitch=71, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=95, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=95, pitch=76, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=95, pitch=79, start=3.375, end=3.75),  # F#
]
piano.notes.extend(piano_notes)

# Sax (Dante) - repeat motif with slight variation
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=105, pitch=66, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=105, pitch=69, start=3.75, end=4.125), # A
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line (Marcus) - walking line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),   # D
]
bass.notes.extend(bass_notes)

# Piano (Diane) - comping on 2 and 4
# Bar 4: D7 chord (F#9) on beat 2
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=95, pitch=71, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=95, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=95, pitch=76, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=95, pitch=79, start=4.875, end=5.25),  # F#
]
piano.notes.extend(piano_notes)

# Sax (Dante) - finish the motif
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=105, pitch=66, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=105, pitch=69, start=5.25, end=5.625), # A
]
sax.notes.extend(sax_notes)

# Drums (Bar 4)
# Kick on 1 and 3
drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_kick_2 = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)
drums.notes.extend([drum_kick_1, drum_kick_2])

# Snare on 2 and 4
drum_snare_1 = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375)
drums.notes.extend([drum_snare_1, drum_snare_2])

# Hi-hats on every eighth
hihat_notes = []
for i in range(0, 6):
    start = (i + 6) * 0.375
    end = start + 0.375
    hihat_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))
drums.notes.extend(hihat_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
