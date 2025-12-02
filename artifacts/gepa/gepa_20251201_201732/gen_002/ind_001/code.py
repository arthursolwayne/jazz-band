
import pretty_midi

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes[0].nominator = 4
pm.time_signature_changes[0].denominator = 4

# Define key: F minor (F, Gb, Ab, Bb, B, Db, Eb)
# We'll use F minor as the key center.

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI file
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)
pm.instruments.append(sax)

# Define timing: 160 BPM, 4/4 time, each bar = 1.5 seconds
# Each beat = 0.375 seconds, each eighth note = 0.1875 seconds

# Create time for each bar (in seconds)
bar_lengths = [1.5, 1.5, 1.5, 1.5]

# --- DRUMS: Little Ray ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

for bar in range(4):
    bar_start = sum(bar_lengths[:bar])
    
    # Kick on 1 and 3
    kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.1875),
                  pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 0.9375)]
    for note in kick_notes:
        drums.notes.append(note)
    
    # Snare on 2 and 4
    snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.5625),
                   pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.3125)]
    for note in snare_notes:
        drums.notes.append(note)
    
    # Hihat on every eighth
    hihat_notes = [pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * 0.1875, end=bar_start + i * 0.1875 + 0.0625)
                   for i in range(8)]
    for note in hihat_notes:
        drums.notes.append(note)

# --- BASS: Marcus ---
# Walking line in F minor (F, Gb, Ab, Bb, B, Db, Eb)
# Root and fifth with chromatic approaches. Key is Fm: F, Ab, Bb, Db, Eb, F, Ab...

bass_notes = [
    # Bar 1
    pretty_midi.Note(velocity=80, pitch=53, start=0, end=0.375),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=58, start=0.375, end=0.75),  # Ab2 (fifth)
    pretty_midi.Note(velocity=80, pitch=57, start=0.75, end=1.125),  # Gb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=53, start=1.125, end=1.5),  # F2 (root)
    
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=58, start=1.875, end=2.25),  # Ab2 (fifth)
    pretty_midi.Note(velocity=80, pitch=59, start=2.25, end=2.625),  # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3),  # F2 (root)
    
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=53, start=3, end=3.375),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=58, start=3.375, end=3.75),  # Ab2 (fifth)
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.125),  # Gb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=53, start=4.125, end=4.5),  # F2 (root)
    
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=58, start=4.875, end=5.25),  # Ab2 (fifth)
    pretty_midi.Note(velocity=80, pitch=59, start=5.25, end=5.625),  # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=6),  # F2 (root)
]

for note in bass_notes:
    bass.notes.append(note)

# --- PIANO: Diane ---
# Open voicings, different chord each bar, resolve on the last.
# Comp on 2 and 4.

# Bar 1: Fm7 (F, Ab, Bb, Db)
# Comp on 2 and 4
piano_notes = [
    # Bar 1 - 2nd beat
    pretty_midi.Note(velocity=100, pitch=64, start=0.375, end=0.5625),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=0.375, end=0.5625),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=0.375, end=0.5625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=0.375, end=0.5625),  # Db4

    # Bar 1 - 4th beat
    pretty_midi.Note(velocity=100, pitch=64, start=1.125, end=1.3125),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=1.125, end=1.3125),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.125, end=1.3125),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=1.125, end=1.3125),  # Db4

    # Bar 2: Bb7 (Bb, Db, F, Ab)
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0625),  # Db4
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0625),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0625),  # Ab4

    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.8125),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.8125),  # Db4
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.8125),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.8125),  # Ab4

    # Bar 3: Eb7 (Eb, Gb, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5625),  # Eb4
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.5625),  # Gb4
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625),  # Db4

    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.3125),  # Eb4
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.3125),  # Gb4
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.3125),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.3125),  # Db4

    # Bar 4: Fm7 (F, Ab, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0625),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.0625),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.0625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0625),  # Db4

    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.8125),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=5.8125),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=5.8125),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=5.8125),  # Db4
]

for note in piano_notes:
    piano.notes.append(note)

# --- SAX: Dante ---
# One short motif. Start it, leave it hanging. Come back and finish it.
# No scale runs. Keep it alive, mysterious, human.

# Bar 1: Play a motif, leave it hanging.

# Motif: F (53) - Ab (58) - rest - F (53)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=0, end=0.375),  # F2
    pretty_midi.Note(velocity=100, pitch=58, start=0.375, end=0.75),  # Ab2
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=58, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=100, pitch=53, start=3, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=58, start=3.375, end=3.75),  # Ab2
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=58, start=4.875, end=5.25),  # Ab2
]

for note in sax_notes:
    sax.notes.append(note)

# Write the MIDI file
pm.write("dante_russo_intro.mid")

print("MIDI file written as 'dante_russo_intro.mid'")
