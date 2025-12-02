
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3
drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick_2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.extend([drum_kick_1, drum_kick_2])

# Snare on 2 and 4
drum_snare_1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drums.notes.extend([drum_snare_1, drum_snare_2])

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.375
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
    drums.notes.append(hihat)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # A
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
# Bar 2: D7 on 2, G7 on 4
# D7: D F# A C
# G7: G B D F
diane_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F#
    
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),   # B
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),   # F
]
piano.notes.extend(diane_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
drum_kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_kick_4 = pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)
drums.notes.extend([drum_kick_3, drum_kick_4])

drum_snare_3 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drum_snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375)
drums.notes.extend([drum_snare_3, drum_snare_4])

for i in range(4, 8):
    start = i * 0.375
    end = start + 0.375
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
    drums.notes.append(hihat)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking bass line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # D
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
# Bar 3: C7 on 2, F7 on 4
# C7: C E G Bb
# F7: F A C Eb
diane_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # Bb
    
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),   # Eb
]
piano.notes.extend(diane_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 3 (3.0 - 4.5s)
drum_kick_5 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_kick_6 = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)
drums.notes.extend([drum_kick_5, drum_kick_6])

drum_snare_5 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
drum_snare_6 = pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875)
drums.notes.extend([drum_snare_5, drum_snare_6])

for i in range(8, 12):
    start = i * 0.375
    end = start + 0.375
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
    drums.notes.append(hihat)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking bass line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
# Bar 4: D7 on 2, G7 on 4
# D7: D F# A C
# G7: G B D F
diane_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # F#
    
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),   # G
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),   # B
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),   # A
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0),   # F
]
piano.notes.extend(diane_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 4 (4.5 - 6.0s)
drum_kick_7 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_kick_8 = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)
drums.notes.extend([drum_kick_7, drum_kick_8])

drum_snare_7 = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
drum_snare_8 = pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375)
drums.notes.extend([drum_snare_7, drum_snare_8])

for i in range(12, 16):
    start = i * 0.375
    end = start + 0.375
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
    drums.notes.append(hihat)

# Dante's motif: Start on 1.5s (beginning of bar 2)
# D (62), F# (66), A (69), G (67) - short motif, leave it hanging

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),   # G
]
sax.notes.extend(sax_notes)

# Repeat motif at 4.5s (start of bar 4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.625, end=4.75),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0),   # G
]
sax.notes.extend(sax_notes)

# Finish the motif on the last bar (6.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.125),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=5.125, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.375),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.375, end=5.5),   # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
