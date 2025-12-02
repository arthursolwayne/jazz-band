
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

bar_length = 1.5  # seconds per bar at 160 BPM

# Bar 1: Drums only
for i in range(2):  # two beats per bar
    # Kick on beat 1 and 3
    if i == 0:
        kick = pretty_midi.Note(velocity=100, pitch=36, start=i * bar_length, end=i * bar_length + 0.375)
        drums.notes.append(kick)
        snare = pretty_midi.Note(velocity=100, pitch=38, start=i * bar_length + 0.75, end=i * bar_length + 1.125)
        drums.notes.append(snare)
    # Hihat on every eighth
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=i * bar_length + i * 0.375, end=i * bar_length + i * 0.375 + 0.125)
    drums.notes.append(hihat)

# Bar 2: Full band (1.5 - 3.0s)
# Bass: Walking line in Fm, roots and fifths, chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25), # G (fifth)
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625), # E♭ (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),  # A♭ (root + 3)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),   # A♭
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),   # D♭
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25), # B♭
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=3.0),  # B♭
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full band (3.0 - 4.5s)
# Bass: Walking line in Fm, roots and fifths, chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # A♭ (root + 3)
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75), # B♭ (fifth)
    pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.125), # G (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5),  # D♭ (root + 3)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: D♭7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),   # D♭
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),   # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),   # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),   # E♭
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),  # E♭
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125), # E♭
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),  # G
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full band (4.5 - 6.0s)
# Bass: Walking line in Fm, roots and fifths, chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875),  # D♭ (root + 3)
    pretty_midi.Note(velocity=90, pitch=59, start=4.875, end=5.25), # E♭ (fifth)
    pretty_midi.Note(velocity=90, pitch=56, start=5.25, end=5.625), # D (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),  # G (root + 3)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Fm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=6.0),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),   # C
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0),   # A♭
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),   # D♭
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25), # B♭
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),  # B♭
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 3 and 4
for bar in range(2):
    bar_start = 3.0 + bar * bar_length
    for i in range(2):  # two beats per bar
        # Kick on beat 1 and 3
        if i == 0:
            kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + i * bar_length, end=bar_start + i * bar_length + 0.375)
            drums.notes.append(kick)
            snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + i * bar_length + 0.75, end=bar_start + i * bar_length + 1.125)
            drums.notes.append(snare)
        # Hihat on every eighth
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * bar_length + i * 0.375, end=bar_start + i * bar_length + i * 0.375 + 0.125)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
